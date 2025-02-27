def composite_nums_between_indices(nums):
    return {num for num in nums[111:112] if num > 1 and (not all((num % i for i in range(2, num))))}