def composite_nums_between_indices(nums):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    start_index = 0
    end_index = 0
    composite_nums = set()
    for i in range(start_index, end_index + 1):
        if i < len(nums) and is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums