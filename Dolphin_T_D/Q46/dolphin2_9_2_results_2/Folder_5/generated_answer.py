def gcf_three_nums(nums_list):
    a = nums_list[64]
    b = nums_list[80]
    c = nums_list[15]
    if a < b:
        a, b = (b, a)
    while b:
        a, b = (b, a % b)
    if a < c:
        c, a = (a, c)
    while c:
        a, c = (c, a % c)
    return a