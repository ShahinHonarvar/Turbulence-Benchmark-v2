def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[55]
    truncatable_primes = set()
    for num in range(10, x):
        num_str = str(num)
        truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - i])):
                truncatable = False
                break
        if truncatable:
            truncatable_primes.add(num)
    return sorted(list(truncatable_primes), reverse=True)