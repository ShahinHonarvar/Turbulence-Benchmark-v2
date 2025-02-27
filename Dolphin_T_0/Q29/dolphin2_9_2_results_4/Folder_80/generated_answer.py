def gcf_two_nums(list_of_nums):
    a = list_of_nums[95]
    b = list_of_nums[85]
    if a == 0:
        return b
    else:
        return gcf_two_nums([b % a])