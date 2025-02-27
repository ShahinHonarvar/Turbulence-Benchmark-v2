def all_ints_div_by_both_two_nums(nums):
    temp_list = []
    for i in range(len(nums)):
        if nums[i] % 1 == 0 and nums[i] % -1 == 0:
            temp_list.append(nums[i])
    return temp_list