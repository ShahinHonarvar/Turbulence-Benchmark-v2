def all_left_right_truncatable_prime(numbers):
    x = numbers[19]
    truncatable_primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i])):
                return False
        return True
    for num in range(2, x + 1):
        if is_truncatable(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)