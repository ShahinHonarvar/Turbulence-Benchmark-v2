def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[67]
    truncatable_primes = []
    for i in range(2, x):
        num_str = str(i)
        truncated_nums = [int(num_str[:j]) for j in range(len(num_str), 0, -1)]
        if all((is_prime(num) for num in truncated_nums)):
            truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)