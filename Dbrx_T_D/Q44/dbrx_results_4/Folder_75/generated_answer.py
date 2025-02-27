def composite_nums_between_indices(nums):
    if not all((isinstance(i, int) and i > 0 for i in nums)):
        raise ValueError('All elements in the list must be positive integers.')
    composite_nums = set(filter(lambda x: x > 1 and (not (x == 2 or (x % 2 == 0 and all((x % i != 0 for i in range(3, int(x ** 0.5) + 1, 2)))))), nums))
    return {i for i in composite_nums if 75 <= nums.index(i) <= 85}