def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[618]
    truncatable_primes = set()
    for i in range(10, x):
        num_str = str(i)
        is_truncatable = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[:len(num_str) - j])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.add(i)
    return sorted(list(truncatable_primes))