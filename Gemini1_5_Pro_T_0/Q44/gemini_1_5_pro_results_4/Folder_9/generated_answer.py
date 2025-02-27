def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(80, len(nums))):
        if i < 80 or i > 200 or nums[i] <= 1:
            continue
        is_composite = False
        for j in range(2, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(nums[i])
    return composite_nums