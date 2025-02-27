def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[945]
    right_truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            num_str = str(i)
            truncated_nums = [int(num_str[:j]) for j in range(1, len(num_str))]
            if all((is_prime(num) for num in truncated_nums)):
                right_truncatable_primes.append(i)
    return sorted(right_truncatable_primes, reverse=True)