def all_left_right_truncatable_prime(nums: tuple[int, ...]) -> list[int]:

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
    x = nums[20]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    left_right_truncatable_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes