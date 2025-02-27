def all_ints_not_div_by_num(nums):
    """Return the list of all values in the list which are not divisible by a given number"""
    filtered_list = []
    for num in nums[43:77]:
        if num % 84 != 0:
            filtered_list.append(num)
    return filtered_list