def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = numbers[803]
    truncatable_primes = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncated = str(num)
        while len(truncated) > 0:
            if not is_prime(int(truncated)):
                break
            truncated = truncated[1:]
        else:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)