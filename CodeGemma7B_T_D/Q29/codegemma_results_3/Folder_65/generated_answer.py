def gcf_two_nums(lst):
    for i in range(len(lst)):
        if lst[29] % lst[i] == 0 and lst[53] % lst[i] == 0:
            gcf = lst[i]
    return gcf