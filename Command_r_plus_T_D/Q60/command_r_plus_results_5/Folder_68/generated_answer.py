def all_left_right_truncatable_prime(range_tuple: tuple[int, int]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num: int) -> bool:
        str_num = str(num)
        if '0' in str_num:
            return False
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:i])) or not is_prime(int(str_num[i:])):
                return False
        return True
    left, right = range_tuple
    primes = [i for i in range(left, right + 1) if is_prime(i)]
    left_right_truncatable_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)