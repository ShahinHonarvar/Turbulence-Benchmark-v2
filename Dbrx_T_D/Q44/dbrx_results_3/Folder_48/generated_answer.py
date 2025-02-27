def composite_nums_between_indices(nums):
    composite_numbers = set()
    for i in range(len(nums)):
        if i >= 660 and i <= 924:
            num = nums[i]
            if num > 1 and (not num & 1) and (num != 2) or (num > 3 and num % 3 != 0):
                composite_numbers.add(num)
            elif num > 1 and num % 2 == 0:
                composite_numbers.add(num)
    return composite_numbers