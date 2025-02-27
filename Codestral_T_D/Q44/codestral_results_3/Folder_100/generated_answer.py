def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(12, 93):
        num = nums[i]
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                composite_nums.add(num)
                break
    return composite_nums