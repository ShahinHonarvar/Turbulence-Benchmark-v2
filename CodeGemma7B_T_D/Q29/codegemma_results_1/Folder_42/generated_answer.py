def gcf_two_nums(list_of_nums):
    a = list_of_nums[90]
    b = list_of_nums[84]
    while b != 0:
        t = b
        b = a % b
        a = t
    return a