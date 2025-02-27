def gcf_three_nums(list_of_nums):
    a = list_of_nums[93]
    b = list_of_nums[94]
    c = list_of_nums[57]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a