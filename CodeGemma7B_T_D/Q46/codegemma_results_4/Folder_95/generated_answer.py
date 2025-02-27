def gcf_three_nums(list):
    a, b, c = (list[87], list[20], list[36])
    common = min(a, b, c)
    while common != 0:
        if a % common == 0 and b % common == 0 and (c % common == 0):
            return common
        common -= 1
    return 1