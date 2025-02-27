def all_right_truncatable_prime(nums):
    x = nums[38]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(x - 1, 0, -1):
        n = i
        is_truncatable = True
        while n > 0:
            if not is_prime(n):
                is_truncatable = False
                break
            n //= 10
        if is_truncatable:
            result.append(i)
    return sorted(result, reverse=True)