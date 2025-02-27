def gcf_two_nums(list_of_nums):
    a = list_of_nums[618]
    b = list_of_nums[195]
    while b:
        a, b = (b, a % b)
    return a