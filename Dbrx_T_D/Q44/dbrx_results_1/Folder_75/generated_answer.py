def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(len(nums)):
        if i >= 75 and i <= 85:
            num = nums[i]
            if num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0):
                composite_numbers.add(num)
    return composite_numbers