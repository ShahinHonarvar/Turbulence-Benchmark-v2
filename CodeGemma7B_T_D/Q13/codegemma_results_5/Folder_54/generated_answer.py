def find_second_largest_num(list_of_nums):
    if len(list_of_nums) <= 34 or len(list_of_nums) > 55:
        return 'None'
    list_of_nums.sort(reverse=True)
    return list_of_nums[34:56][1]