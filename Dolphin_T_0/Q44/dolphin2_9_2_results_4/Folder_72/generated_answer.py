def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(55, 99):
        num = nums[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    composite_nums.add(num)
                    break
    return composite_nums