def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(26, len(nums))):
        n = nums[i] if i < len(nums) else 1
        is_composite = False
        if n > 3:
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_composite = True
                    break
        if is_composite and i <= 52:
            composite_nums.add(n)
    return composite_nums