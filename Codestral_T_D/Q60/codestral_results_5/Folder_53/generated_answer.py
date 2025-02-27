def all_left_right_truncatable_prime(numbers):
    x = numbers[86]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        num_str = str(n)
        for _ in range(len(num_str)):
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:]
            if len(num_str) == 1 and int(num_str) in [2, 3, 5, 7]:
                break
        num_str = str(n)
        for _ in range(len(num_str)):
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
            if len(num_str) == 1 and int(num_str) in [2, 3, 5, 7]:
                break
        return True
    left_right_truncatable_primes = [n for n in range(2, x + 1) if is_left_right_truncatable_prime(n)]
    return sorted(left_right_truncatable_primes, reverse=True)