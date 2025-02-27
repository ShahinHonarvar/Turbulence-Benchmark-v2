def gcf_three_nums(nums_list):
    a = nums_list[20]
    b = nums_list[17]
    c = nums_list[28]
    for i in range(min(a, b, c), 1, -1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i