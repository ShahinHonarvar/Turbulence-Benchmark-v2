def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(0, 29), min(len(nums), 80)):
        n = nums[i]
        if n > 1:
            is_composite = False
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_composite = True
                    break
            if is_composite:
                composite_nums.add(n)
    return composite_nums