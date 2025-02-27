def composite_nums_between_indices(nums):
    res = set()
    for i in range(max(0, 527), min(len(nums), 539)):
        n = nums[i]
        if n <= 1:
            continue
        is_composite = False
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                is_composite = True
                break
        if is_composite:
            res.add(n)
    return res