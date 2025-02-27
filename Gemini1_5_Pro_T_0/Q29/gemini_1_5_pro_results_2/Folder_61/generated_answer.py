def gcf_two_nums(list_of_nums):
    a = list_of_nums[8]
    b = list_of_nums[3]
    while b:
        a, b = (b, a % b)
    return a