def all_ints_div_by_num(nums):
    new_list = []
    for num in nums[160:971]:
        if num % 763 == 0:
            new_list.append(num)
    if not new_list:
        return []
    return new_list