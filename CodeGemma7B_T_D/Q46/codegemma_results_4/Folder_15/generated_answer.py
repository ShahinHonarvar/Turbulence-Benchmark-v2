def gcf_three_nums(num_list):
    a = num_list[4]
    b = num_list[0]
    c = num_list[8]
    temp = min(a, b)
    while temp > 0:
        if a % temp == 0 and b % temp == 0 and (c % temp == 0):
            return temp
        temp -= 1