def all_left_truncatable_prime(x_tuple):
    x = x_tuple[49]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            truncated_num = int(str_num[i:])
            if not is_prime(truncated_num):
                return False
        return True
    left_truncatable_primes = [num for num in range(x) if is_left_truncatable_prime(num)]
    return sorted(left_truncatable_primes)