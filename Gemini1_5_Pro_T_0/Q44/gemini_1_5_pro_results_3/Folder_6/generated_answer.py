def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(13, len(nums))):
        for j in range(min(68, len(nums)) + 1):
            n = nums[j]
            if n > 1:
                is_composite = False
                for k in range(2, int(n ** 0.5) + 1):
                    if n % k == 0:
                        is_composite = True
                        break
                if is_composite:
                    composite_nums.add(n)
    return composite_nums