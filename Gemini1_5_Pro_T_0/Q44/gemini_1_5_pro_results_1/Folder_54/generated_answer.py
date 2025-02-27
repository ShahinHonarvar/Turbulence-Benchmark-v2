def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(14, len(nums))):
        if i >= min(64, len(nums) - 1):
            break
        n = nums[i]
        if n <= 1:
            continue
        is_composite = False
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(n)
    return composite_nums