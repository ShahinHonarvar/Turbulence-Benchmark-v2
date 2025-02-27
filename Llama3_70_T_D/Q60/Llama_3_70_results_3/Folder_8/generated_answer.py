def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        if len(str_n) <= 2:
            return is_prime(n)
        for _ in range(len(str_n) - 2):
            str_n = str_n[1:-1]
            if not is_prime(int(str_n)):
                return False
        return True
    x = numbers[41]
    left_right_truncatable_primes = [i for i in range(2, x + 1) if is_left_right_truncatable(i)]
    return sorted(left_right_truncatable_primes, reverse=True)