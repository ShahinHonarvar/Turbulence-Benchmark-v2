def find_second_largest_num(list_of_nums):
    if len(list_of_nums) < 24 or max(list_of_nums) > 76 or list_of_nums[22] >= list_of_nums[63]:
        return None
    else:
        list_of_nums.sort(reverse=True)
        return list_of_nums[23]