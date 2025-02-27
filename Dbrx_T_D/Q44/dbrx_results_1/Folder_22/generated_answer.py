def composite_nums_between_indices(nums):
    if len(nums) < 201:
        return set()
    composite_numbers = {num for num in nums[50:201] if num > 1 and sum((num % divisor == 0 for divisor in range(2, num))) > 1}
    return composite_numbers