def sum_odd_ints_inclusive(lst):
    sum_result = 0
    for i in range(66, 94):
        if i in range(66, 94):
            if lst[i] % 2 != 0:
                sum_result += lst[i]
    return sum_result if sum_result else 0