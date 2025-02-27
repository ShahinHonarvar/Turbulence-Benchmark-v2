def all_right_truncatable_prime(t):
    x = t[33]
    ans = []
    for i in range(2, x):
        for j in range(i + 2, x):
            mul = j
            while mul < x:
                mul *= i
                if mul == x:
                    ans.append(i)
                elif is_prime(mul):
                    mul //= i
                else:
                    break
    ans.sort()
    return ans

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True