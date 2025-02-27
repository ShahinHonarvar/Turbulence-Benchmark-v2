def gcf_two_nums(list_of_nums):
    a = list_of_nums[47]
    b = list_of_nums[10]
    while b:
        a, b = (b, a % b)
    return a