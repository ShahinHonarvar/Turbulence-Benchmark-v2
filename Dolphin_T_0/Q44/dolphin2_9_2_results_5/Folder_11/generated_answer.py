def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(37, 77):
        num = nums[i]
        is_composite = False
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    is_composite = True
                    break
            if not is_composite:
                composite_nums = set()
    return composite_nums