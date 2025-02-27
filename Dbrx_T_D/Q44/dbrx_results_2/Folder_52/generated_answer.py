def composite_nums_between_indices(nums):
    composite_set = set()
    if len(nums) < 100:
        return composite_set
    for i in range(62, 100):
        num = nums[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    composite_set.add(num)
                    break
    return composite_set