def sum_odd_ints_inclusive(list1):
    total_sum = 0
    count = 0
    for i in range(30, 49):
        if list1[i] % 2 != 0:
            total_sum += list1[i]
            count += 1
    if count == 0:
        return 0
    return total_sum