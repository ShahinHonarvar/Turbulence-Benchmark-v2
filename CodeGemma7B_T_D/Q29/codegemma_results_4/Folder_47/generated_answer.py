def gcf_two_nums(list):
    num_a = list[28]
    num_b = list[17]
    if num_a > num_b:
        smaller_num = num_b
    else:
        smaller_num = num_a
    for i in range(smaller_num):
        if num_a % (smaller_num - i) == 0 and num_b % (smaller_num - i) == 0:
            gcf = smaller_num - i
            break
    if gcf == smaller_num:
        gcf = 1
    return gcf