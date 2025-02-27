def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[0:7]:
        if num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0)):
            composite_nums.add(num)
    return composite_nums if composite_nums else set()