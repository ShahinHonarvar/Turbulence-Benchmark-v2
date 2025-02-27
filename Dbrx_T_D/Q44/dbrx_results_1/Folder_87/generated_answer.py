def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(43, 52):
        if i < len(nums) and nums[i] > 1:
            is_composite = False
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_numbers.add(nums[i])
    return composite_numbers