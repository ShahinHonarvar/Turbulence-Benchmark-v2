def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[618]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncated = str(i)
        is_truncatable = True
        for _ in range(len(truncated) - 1):
            truncated = truncated[1:]
            if not is_prime(int(truncated)):
                is_truncatable = False
                break
        if is_truncatable and is_prime(i):
            left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)