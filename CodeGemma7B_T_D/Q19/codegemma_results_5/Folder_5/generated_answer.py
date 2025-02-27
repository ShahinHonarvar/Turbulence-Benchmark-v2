def all_ints_not_div_by_num(nums):
    lst = []
    for num in nums[1:2]:
        if num % 8 != 0:
            lst.append(num)
    return lst