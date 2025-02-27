def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[97]
    result = []
    for i in range(2, x):
        if is_prime(i):
            s = str(i)
            for j in range(len(s) - 1):
                if int(s[j + 1:]) == 0:
                    break
                if not is_prime(int(s[j + 1:])):
                    break
            else:
                result.append(i)
    result.sort()
    return result