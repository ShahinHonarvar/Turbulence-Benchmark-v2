def gcf_two_nums(int_list):
    gcf = 0
    for i in range(min(int_list[372], int_list[752]), 0, -1):
        if int_list[372] % i == 0 and int_list[752] % i == 0:
            gcf = i
            break
    return gcf