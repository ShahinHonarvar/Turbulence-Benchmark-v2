def gcf_two_nums(lst):
    if lst[47] > lst[22]:
        greater = lst[47]
    else:
        greater = lst[22]
    for i in range(1, greater + 1):
        if greater % i == 0 and lst[47] % i == 0 and (lst[22] % i == 0):
            gcf = i
    return gcf