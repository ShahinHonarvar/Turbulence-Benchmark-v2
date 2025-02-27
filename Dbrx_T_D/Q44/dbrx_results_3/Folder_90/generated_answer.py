def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(333, 369):
        if i < len(nums) and nums[i] > 1 and (not (nums[i] == 2 or (nums[i] % 2 == 0 and nums[i] != 2))):
            is_composite = False
            for j in range(3, int(nums[i] ** 0.5) + 1, 2):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(nums[i])
    return composite_numbers