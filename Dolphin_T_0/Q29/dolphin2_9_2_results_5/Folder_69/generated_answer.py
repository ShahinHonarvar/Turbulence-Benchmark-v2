def gcf_two_nums(lst):
    gcf = 1
    for i in range(1, min(lst[894], lst[801]) + 1):
        if lst[894] % i == 0 and lst[801] % i == 0:
            gcf = i
    return gcf