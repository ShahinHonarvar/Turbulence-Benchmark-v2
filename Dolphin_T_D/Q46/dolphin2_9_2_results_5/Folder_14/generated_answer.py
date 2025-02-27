def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a % b)

def gcf_three_nums(int_list):
    return gcf(gcf(int_list[17], int_list[88]), int_list[35])