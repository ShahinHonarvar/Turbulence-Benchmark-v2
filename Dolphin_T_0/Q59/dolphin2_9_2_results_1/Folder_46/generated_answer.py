def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tp):
    x = tp[33]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            n = i
            while n != 0:
                if not is_prime(n):
                    break
                n //= 10
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)