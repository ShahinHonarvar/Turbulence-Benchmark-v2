def all_left_truncatable_prime(numbers):
    x = numbers[91]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        if not is_prime(n):
            return False
        str_n = str(n)
        for i in range(1, len(str_n)):
            truncated_n = int(str_n[i:])
            if not is_prime(truncated_n):
                return False
        return True
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            primes.append(num)
    return sorted(primes)