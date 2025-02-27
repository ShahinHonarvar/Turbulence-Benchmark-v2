def composite_nums_between_indices(nums):
    res = set()
    for i in range(max(5, len(nums))):
        n = nums[i] if i < len(nums) else 0
        if n > 3 and i >= 5 and (i <= 7):
            is_composite = False
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    is_composite = True
                    break
            if is_composite:
                res.add(n)
    return res