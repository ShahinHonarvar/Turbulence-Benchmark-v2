def all_left_truncatable_prime(t):
    x = t[54]
    left_truncatable_primes = []
    for num in range(x, 0, -1):
        trunc = num
        while trunc:
            if is_prime(trunc) and trunc != 0:
                trunc //= 10
            else:
                break
        else:
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True