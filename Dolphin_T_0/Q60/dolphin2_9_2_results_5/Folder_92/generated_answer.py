def is_prime_n(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True

def is_left_and_right_truncatable_prime(n):
    if n < 10:
        return is_prime_n(n)
    else:
        for i in range(len(str(n)) - 1, 0, -1):
            m = int(str(n)[i])
            if m == 0 or not is_prime_n(n - m):
                return False
        return True

def all_left_right_truncatable_prime(t):
    x = t[7]
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_and_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    return sorted(left_right_truncatable_primes)