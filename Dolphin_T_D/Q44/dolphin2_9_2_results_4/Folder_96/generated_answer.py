def composite_nums_between_indices(nums):
    composite_set = set()
    for i in range(60, 201):
        num = nums[i]
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    composite_set.add(num)
                    break
    return composite_set