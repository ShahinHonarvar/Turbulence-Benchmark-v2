def all_left_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

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
            if not is_prime(int(str_num[:i])) or not is_prime(int(str_num[-i:])) or (not is_prime(int(str_num[i:-i]))):
                return False
        return True
    max_num = numbers[85]
    left_right_truncatable_primes = []
    for num in range(2, max_num + 1):
        if is_left_right_truncatable_prime(num):
            left_right_truncatable_primes.append(num)
    return left_right_truncatable_primes