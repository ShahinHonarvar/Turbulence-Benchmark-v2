def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(max(31, 0), min(len(nums), 73)):
        n = nums[i]
        if n <= 1:
            continue
        is_composite = True
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                is_composite = False
                break
        if is_composite:
            composite_nums.add(n)
    return composite_nums