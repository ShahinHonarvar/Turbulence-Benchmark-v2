def composite_nums_between_indices(nums):

    def is_composite(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    composite_nums = set()
    for i in range(max(1, len(nums))):
        if i < len(nums) and 1 <= i <= 5 and is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums