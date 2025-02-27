def composite_nums_between_indices(nums):
    if not all((isinstance(num, int) and num > 0 for num in nums)):
        raise ValueError('All elements in the list must be positive integers')
    return {num for num in nums[22:64] if num > 1 and any((num % i == 0 for i in range(2, num)))}