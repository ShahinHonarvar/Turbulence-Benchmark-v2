def gcf_two_nums(list_of_nums):
    a = list_of_nums[7]
    b = list_of_nums[9]
    while b:
        a, b = (b, a % b)
    return a