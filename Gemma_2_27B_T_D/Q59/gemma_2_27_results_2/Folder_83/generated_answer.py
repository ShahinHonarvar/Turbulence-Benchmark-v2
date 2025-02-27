def all_left_truncatable_prime(nums):
    x = nums[24]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        if not is_prime(n):
            return False
        while n > 0:
            n //= 10
            if n > 0 and (not is_prime(n)):
                return False
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    return sorted(result)