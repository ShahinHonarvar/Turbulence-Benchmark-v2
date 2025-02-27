def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        while len(str_n) > 2:
            if not is_prime(int(str_n)):
                return False
            str_n = str_n[1:-1]
        return is_prime(int(str_n))
    max_num = numbers[32]
    left_right_truncatable_primes = [n for n in range(2, max_num + 1) if is_prime(n) and is_left_right_truncatable_prime(n)]
    return sorted(left_right_truncatable_primes)