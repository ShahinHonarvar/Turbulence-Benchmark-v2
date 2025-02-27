def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(len(nums)):
        if i < 314 or i > 347:
            continue
        num = nums[i]
        if num == 1:
            continue
        j = 2
        is_composite = False
        while j * j <= num:
            if num % j == 0:
                is_composite = True
                break
            j += 1
        if is_composite:
            composite_set.add(num)
    return composite_set