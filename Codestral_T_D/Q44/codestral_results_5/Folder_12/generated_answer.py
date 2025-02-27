def composite_nums_between_indices(nums):
    composite_nums = {num for num in nums[51:87] if any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}
    return composite_nums