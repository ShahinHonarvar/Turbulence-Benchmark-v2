def composite_nums_between_indices(nums):
    res = set()
    for i in range(max(0, 32), min(len(nums), 36)):
        num = nums[i]
        is_composite = False
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    is_composite = True
                    break
        if is_composite:
            res.add(num)
    return res