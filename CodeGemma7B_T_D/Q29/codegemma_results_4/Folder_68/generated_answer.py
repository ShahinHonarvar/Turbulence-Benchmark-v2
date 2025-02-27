def gcf_two_nums(num_list):
    a, b = (num_list[8], num_list[9])
    common = 0
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            common = i
            break
    return common