def composite_nums_between_indices(nums):
    res = set()
    for i in range(max(0, len(nums) - 1)):
        if i >= 62 and i <= 63:
            n = nums[i]
            is_composite = False
            if n > 1:
                for j in range(2, int(n ** 0.5) + 1):
                    if n % j == 0:
                        is_composite = True
                        break
                if is_composite:
                    res.add(n)
    return res