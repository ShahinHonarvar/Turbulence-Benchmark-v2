def gcf_two_nums(list_of_nums):
    a = list_of_nums[20]
    b = list_of_nums[83]
    while b:
        a, b = (b, a % b)
    return a