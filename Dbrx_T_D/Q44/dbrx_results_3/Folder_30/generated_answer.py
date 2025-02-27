def composite_nums_between_indices(nums):
    if len(nums) < 92:
        return set()
    composite_numbers = {num for num in nums[19:93] if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}
    return composite_numbers.difference({num for num in composite_numbers if num in {2, 3, 5}})