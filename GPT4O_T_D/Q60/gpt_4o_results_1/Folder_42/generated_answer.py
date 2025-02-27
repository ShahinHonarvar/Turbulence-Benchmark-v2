def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def has_zero(n):
        return '0' in str(n)

    def is_left_right_truncatable_prime(n):
        if has_zero(n):
            return False
        num_str = str(n)
        length = len(num_str)
        for i in range(length - 1):
            if not is_prime(int(num_str[i + 1:])) or not is_prime(int(num_str[:length - i - 1])):
                return False
        return True
    x = numbers[64]
    truncatable_primes = []
    for number in range(2, x + 1):
        if is_prime(number) and is_left_right_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)