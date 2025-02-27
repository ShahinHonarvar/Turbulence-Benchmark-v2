def gcf_three_nums(list_of_nums):
    a = list_of_nums[1]
    b = list_of_nums[2]
    c = list_of_nums[7]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a