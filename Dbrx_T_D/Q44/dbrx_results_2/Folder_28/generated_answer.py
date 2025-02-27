def composite_nums_between_indices(nums):
    return {num for num in nums[22:89] if num > 1 and (not all((num % i for i in range(2, num))))}