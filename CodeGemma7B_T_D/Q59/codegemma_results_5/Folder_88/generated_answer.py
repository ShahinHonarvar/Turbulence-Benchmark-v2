def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(x):
    ans = []
    for i in range(x):
        if prime(i):
            flag = True
            for j in range(2, int(i ** 0.5) + 1):
                if prime(int(str(i)[:-1])):
                    flag = False
                    break
            if flag:
                ans.append(i)
    ans.sort()
    return ans