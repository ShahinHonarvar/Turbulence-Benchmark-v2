def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(len(nums)):
        if i >= 42 and i <= 68:
            num = nums[i]
            if num > 1 and (not num.is_prime()):
                composite_numbers.add(num)
    return composite_numbers