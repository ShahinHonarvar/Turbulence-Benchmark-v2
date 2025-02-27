def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(29, 80):
        num = nums[i]
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    composite_nums.add(num)
                    break
    return composite_nums