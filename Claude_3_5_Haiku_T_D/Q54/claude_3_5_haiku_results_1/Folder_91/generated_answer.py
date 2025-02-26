def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[0]
    right_truncatable_primes = []
    for n in range(x - 1, 1, -1):
        truncatable = True
        current = n
        while current > 0:
            if not is_prime(current):
                truncatable = False
                break
            current //= 10
        if truncatable:
            right_truncatable_primes.append(n)
    return right_truncatable_primes