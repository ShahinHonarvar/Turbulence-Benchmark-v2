def composite_nums_between_indices(nums):
    if len(nums) < 53:
        return set()
    composite_numbers = set()
    for i in range(26, 53):
        if nums[i] > 1:
            for j in range(2, nums[i]):
                if nums[i] % j == 0:
                    composite_numbers.add(nums[i])
                    break
    return composite_numbers