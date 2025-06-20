def all_left_right_truncatable_prime(numbers: tuple[int, int, int, int, int]) -> list[int]:

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
        for i in range(1, len(str(num))):
            if not is_prime(int(str(num)[:i])) or not is_prime(int(str(num)[i:])):
                return False
        return True
    max_val = numbers[4]
    left_right_primes = []
    for num in range(2, max_val + 1):
        if is_prime(num) and is_left_right_truncatable_prime(num):
            left_right_primes.append(num)
    return left_right_primes