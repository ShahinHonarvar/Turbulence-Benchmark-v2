def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    def is_right_truncatable(n):
        str_n = str(n)
        for i in range(len(str_n), 0, -1):
            if not is_prime(int(str_n[:i])):
                return False
        return True
    x = nums[61]
    right_truncatable_primes = [i for i in range(2, x) if is_right_truncatable(i)]
    return sorted(right_truncatable_primes)