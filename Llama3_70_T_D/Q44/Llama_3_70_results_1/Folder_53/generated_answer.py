def composite_nums_between_indices(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    composite_nums = set()
    for i in range(222, 222 + 1):
        if i < len(nums):
            num = nums[i]
            if not is_prime(num):
                composite_nums.add(num)
    return composite_nums