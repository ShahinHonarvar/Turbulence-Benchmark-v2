def composite_nums_between_indices(nums):
    res = set()
    for i in range(max(0, 533), min(len(nums), 606)):
        num = nums[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    res.add(num)
                    break
    return res