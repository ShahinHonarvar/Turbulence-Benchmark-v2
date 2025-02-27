def gcf(a, b):
    if a % b == 0:
        return b
    return gcf(b, a % b)

def gcf_three_nums(numb_list):
    return gcf(gcf(numb_list[70], numb_list[41]), numb_list[20])