def all_left_truncatable_prime(nums):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        while num > 0:
            if not is_prime(num):
                return False
            num //= 10
        return True
    if len(nums) <= 54:
        return []
    x = nums[54]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable(num):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)