def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(51, len(nums))):
        if i >= 51 and i <= 86:
            n = nums[i]
            is_composite = False
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_composite = True
                    break
            if is_composite and n > 1:
                composite_nums.add(n)
    return composite_nums