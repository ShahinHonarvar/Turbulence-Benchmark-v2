def all_left_truncatable_prime(nums):
    nums = sorted(nums)[::-1]

    def is_left_truncatable_prime(n):
        if n == 0:
            return False
        for d in str(n):
            if d == '0':
                return False
            elif d not in '2357':
                return False
        return True
    left_trunc_primes = []
    for i in range(len(nums)):
        if is_left_truncatable_prime(nums[i] - 1):
            left_trunc_prime = nums[i] - 1
            left_trunc_primes.append(left_trunc_prime)
    return left_trunc_primes