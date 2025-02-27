def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[54]
    left_truncatable_primes = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i):
            truncated = str(i)[1:]
            while truncated:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[1:]
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)