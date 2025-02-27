def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncatable(n):
        num_str = str(n)
        while len(num_str) > 0:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    x = numbers[61]
    truncatable_primes = []
    for n in range(2, x + 1):
        if '0' not in str(n) and is_left_truncatable(n) and is_right_truncatable(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes)