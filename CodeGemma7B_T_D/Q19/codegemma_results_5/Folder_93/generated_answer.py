def all_ints_not_div_by_num(nums):
    new_list = []
    for num in nums[33:78]:
        if num and num % -17:
            new_list.append(num)
    return new_list