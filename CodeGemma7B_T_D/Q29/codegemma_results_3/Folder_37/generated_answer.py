def gcf_two_nums(num_list):
    a = num_list[29]
    b = num_list[74]
    common = None
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            common = i
            break
    return common