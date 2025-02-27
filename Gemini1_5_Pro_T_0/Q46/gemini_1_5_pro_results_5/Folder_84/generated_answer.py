def gcf_three_nums(list_of_nums):
    a = list_of_nums[695]
    b = list_of_nums[710]
    c = list_of_nums[914]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a