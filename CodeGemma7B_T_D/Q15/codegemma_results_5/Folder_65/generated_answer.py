def sum_odd_ints_inclusive(list1):
    final_sum = 0
    for i in range(56, 99):
        if list1[i] % 2 != 0:
            final_sum += list1[i]
    if final_sum == 0:
        return 0
    else:
        return final_sum