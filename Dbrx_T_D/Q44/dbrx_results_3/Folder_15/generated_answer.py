def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(min(3, len(nums)), min(4, len(nums))):
        num = nums[i]
        if num > 1 and (not num % (num - 1) % (num - 2) == 0):
            composite_numbers.add(num)
    return composite_numbers