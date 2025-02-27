def composite_nums_between_indices(nums):
    result = set()
    for i in range(max(8, len(nums))):
        if i < 8 or i > 9:
            continue
        num = nums[i]
        if num <= 1:
            continue
        is_composite = False
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                is_composite = True
                break
        if is_composite:
            result.add(num)
    return result