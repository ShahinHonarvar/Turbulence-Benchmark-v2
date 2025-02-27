def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(p):
    p_str = str(p)
    for i in range(len(p_str) - 1, 0, -1):
        if not is_prime(int(p_str[i:])):
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[41]
    primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            if is_truncatable(num):
                primes.append(num)
    return primes