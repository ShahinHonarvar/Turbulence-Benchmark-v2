def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        num_str = str(n)
        if '0' in num_str:
            return False
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:-i or len(num_str)])):
                return False
        return True
    x = numbers[36]
    truncatable_primes = [i for i in range(11, x + 1) if is_prime(i) and is_truncatable(i)]
    return truncatable_primes