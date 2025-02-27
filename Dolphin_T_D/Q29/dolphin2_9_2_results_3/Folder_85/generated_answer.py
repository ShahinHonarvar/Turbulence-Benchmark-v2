def gcf_two_nums(nums_list):
    a = nums_list[38]
    b = nums_list[77]
    if a < b:
        a, b = (b, a)
    while b:
        a, b = (b, a % b)
    return a