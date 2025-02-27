def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        n_str = str(n)
        for i in range(1, len(n_str)):
            truncated_n = int(n_str[i:])
            if not is_prime(truncated_n):
                return False
        return True
    x = numbers[803]
    left_truncatable_primes = []
    for n in range(2, x):
        if is_left_truncatable(n):
            if is_prime(n):
                left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)