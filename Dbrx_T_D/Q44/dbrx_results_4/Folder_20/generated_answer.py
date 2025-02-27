def composite_nums_between_indices(nums):
    if not all((isinstance(i, int) and i > 0 for i in nums)):
        raise ValueError('All elements in the list must be positive integers')
    if len(nums) < 95:
        raise IndexError('List length must be at least 95')
    composite_numbers = set()
    for i, num in enumerate(nums[74:96]):
        if num > 1 and (not (num == 2 or (num % 2 == 0 and num * num > i * i + i * j))):
            composite_numbers.add(num)
    return composite_numbers