def composite_nums_between_indices(nums):

    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composite_nums = set()
    for i in range(max(1, len(nums) - 4)):
        if is_composite(nums[i + 1]):
            composite_nums.add(nums[i + 1])
    return composite_nums