def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[760]
    truncatable_primes = []
    for num in range(2, x):
        num_str = str(num)
        is_truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[:i + 1])):
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)