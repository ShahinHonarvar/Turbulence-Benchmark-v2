def gcf_two_nums(list_of_nums):
    a = list_of_nums[85]
    b = list_of_nums[51]
    while b:
        a, b = (b, a % b)
    return a