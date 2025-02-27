def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[20]
    result = []
    for i in range(2, x):
        if '0' in str(i):
            continue
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num //= 10
        if num == 0:
            result.append(i)
    return sorted(result, reverse=True)