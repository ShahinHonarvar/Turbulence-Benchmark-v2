def composite_nums_between_indices(nums):
    return {num for num in nums[8:10] if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}