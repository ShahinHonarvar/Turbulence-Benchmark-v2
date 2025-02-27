def composite_nums_between_indices(nums):
    return {n for n in nums[31:72 + 1] if n != 1 and n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or (n % 7 == 0)}