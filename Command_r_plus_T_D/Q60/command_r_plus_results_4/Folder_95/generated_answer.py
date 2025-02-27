def all_left_right_truncatable_prime(numbers: tuple[int, ...]) -> list[int]:

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num: int) -> bool:
        if str(num).count('0') > 0:
            return False
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[:i])) or not is_prime(int(str(num)[i:])):
                return False
        return True
    upper_bound = numbers[77]
    left_right_primes = [num for num in range(2, upper_bound + 1) if is_left_right_truncatable_prime(num)]
    return sorted(left_right_primes)