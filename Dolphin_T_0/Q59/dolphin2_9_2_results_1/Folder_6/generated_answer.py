def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[74]
    primes = [2, 3, 5, 7]
    for i in range(10, x):
        s = str(i)
        for j in s:
            if j == '0':
                break
        else:
            if is_prime(i) and all((is_prime(int(s[:j])) for j in range(1, len(s)))):
                primes.append(i)
    return sorted(primes)