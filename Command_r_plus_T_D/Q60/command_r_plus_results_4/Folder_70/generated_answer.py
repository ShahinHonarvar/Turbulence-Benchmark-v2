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
            if not is_prime(int(str_num[:i])) or not is_prime(int(str_num[i:])):
                return False
        return True
    max_num = numbers[433]
    truncatable_primes = []
    for num in range(max_num, 0, -1):
        if is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
        if len(str(num)) <= 2:
            break
    return sorted(truncatable_primes, reverse=True)