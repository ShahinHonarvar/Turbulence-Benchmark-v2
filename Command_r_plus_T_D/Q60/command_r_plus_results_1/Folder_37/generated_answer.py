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
            if not is_prime(int(str(num)[:i]) if i < len(str(num)) - 1 else num) or not is_prime(int(str(num)[i + 1:]) if i < len(str(num)) - 1 else num):
                return False
        return True
    x = numbers[35]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    return sorted(left_right_truncatable_primes, reverse=True)