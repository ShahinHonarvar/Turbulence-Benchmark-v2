def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(len(nums)):
        if i >= 29 and i <= 51:
            num = nums[i]
            if num > 1 and (not num.is_prime()):
                composite_nums.add(num)
    return composite_nums