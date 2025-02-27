def gcf_two_nums(list):
    list_64_28 = list[64] * list[28]
    gcf = 1
    for j in range(2, min(list_64_28, gcf) + 1):
        if list_64_28 % j == 0 and gcf % j == 0:
            gcf = j
    return gcf