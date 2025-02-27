def all_ints_div_by_both_two_nums(nums):
    list = []
    for num in nums[20:36]:
        if num % 36 == 0 and num % 89 == 0:
            list.append(num)
    return list