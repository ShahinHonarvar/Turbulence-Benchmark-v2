def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(len(nums)):
        if i in range(0, 3):
            if not (nums[i] == 2 or nums[i] == 3):
                if any((num % divisor == 0 for divisor in range(2, int(nums[i] ** 0.5) + 1))):
                    composite_set.add(nums[i])
    return composite_set