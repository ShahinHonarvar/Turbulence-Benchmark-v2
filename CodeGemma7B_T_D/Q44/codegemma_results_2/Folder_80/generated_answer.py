def composite_nums_between_indices(nums):
    composite_set = set()
    for num in nums[62:79]:
        if num % 2 != 0 and (num % 3 == 0 or num % 5 == 0 or num % 7 == 0):
            composite_set.add(num)
    return composite_set