def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for num in list_of_nums[667:775]:
        if num % 1 != 0 and num % 2 != 0 and (num % 3 != 0) and (num % 5 != 0) and (num % 7 != 0) and (num % 11 != 0) and (num % 13 != 0) and (num % 17 != 0) and (num % 19 != 0):
            composite_nums.add(num)
    return composite_nums