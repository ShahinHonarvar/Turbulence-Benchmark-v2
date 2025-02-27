def gcf_three_nums(lst):
    gcf = 0
    for i in range(min(lst[92], lst[69], lst[95]), 0, -1):
        if lst[92] % i == 0 and lst[69] % i == 0 and (lst[95] % i == 0):
            gcf = i
            break
    return gcf