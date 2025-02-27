def all_left_truncatable_prime(t):
    x = t[41]
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            temp = i
            while temp > 0:
                if not isprime(temp):
                    break
                temp //= 10
            else:
                result.append(i)
    return sorted(result)

def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True