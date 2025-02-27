def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    if len(nums) <= 86:
        return []
    limit = nums[86]

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        s = str(n)
        for i in range(len(s), 0, -1):
            if not is_prime(int(s[:i])):
                return False
        return True
    truncatable_primes = [n for n in range(2, limit) if is_right_truncatable_prime(n)]
    return sorted(truncatable_primes, reverse=True)