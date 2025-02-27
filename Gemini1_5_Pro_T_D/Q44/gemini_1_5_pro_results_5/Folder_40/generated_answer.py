def composite_nums_between_indices(nums):
    result = set()
    for i in range(2, 3):
        if i >= len(nums) or nums[i] <= 1:
            continue
        is_composite = False
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                is_composite = True
                break
        if is_composite:
            result.add(nums[i])
    return result