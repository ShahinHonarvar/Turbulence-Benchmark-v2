def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(list):
    return gcf(gcf(list[20], list[51]), list[62])