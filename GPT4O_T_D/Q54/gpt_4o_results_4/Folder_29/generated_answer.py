def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    if len(nums) <= 55:
        return []
    x = nums[55]

    def is_right_truncatable_prime(p):
        str_p = str(p)
        for i in range(len(str_p)):
            if not is_prime(int(str_p[:len(str_p) - i])):
                return False
        return True
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes, reverse=True)