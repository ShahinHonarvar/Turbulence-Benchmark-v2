def composite_nums_between_indices(nums):
    result = set()
    for i in range(max(17, 0), min(79, len(nums))):
        n = nums[i]
        if n <= 1:
            continue
        is_composite = False
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                is_composite = True
                break
        if is_composite:
            result.add(n)
    return result