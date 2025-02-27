def all_ints_div_by_both_two_nums(nums):
    new_lst = []
    for num in nums:
        if num % -33 == 0 and num % -62 == 0 and (num in nums[81:87]):
            new_lst.append(num)
    return new_lst