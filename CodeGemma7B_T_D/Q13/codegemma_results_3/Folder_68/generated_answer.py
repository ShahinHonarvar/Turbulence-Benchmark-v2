def find_second_largest_num(list_nums):
    if len(list_nums) <= 8:
        return None
    list_nums.sort(reverse=True)
    return list_nums[1]