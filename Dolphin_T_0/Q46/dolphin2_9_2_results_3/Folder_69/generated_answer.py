def gcf_three_nums(num_list):
    a = num_list[404]
    b = num_list[834]
    c = num_list[517]
    i = 1
    while i <= min(a, b, c):
        if a % i == b % i == c % i == 0:
            gcf = i
        i += 1
    return gcf