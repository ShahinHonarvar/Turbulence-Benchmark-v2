def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(69, 84):
        num = nums[i]
        if num > 1:
            for divisor in range(2, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    composite_nums.add(num)
                    break
    return composite_nums