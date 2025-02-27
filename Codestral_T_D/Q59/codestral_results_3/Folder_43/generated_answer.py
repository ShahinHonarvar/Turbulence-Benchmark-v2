def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[89]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i):
            if is_prime(i):
                num = i
                while num:
                    num //= 10
                    if not is_prime(num):
                        break
                else:
                    left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)