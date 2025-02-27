def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[78]
    right_truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            truncated = str_num
            while truncated and is_prime(int(truncated)):
                truncated = truncated[:-1]
            if not truncated:
                right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes, reverse=True)