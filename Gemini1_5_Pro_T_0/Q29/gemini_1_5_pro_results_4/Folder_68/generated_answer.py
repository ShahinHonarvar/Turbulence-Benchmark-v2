def gcf_two_nums(list_of_nums):
    a = list_of_nums[8]
    b = list_of_nums[9]
    while a:
        a, b = (b % a, a)
    return b