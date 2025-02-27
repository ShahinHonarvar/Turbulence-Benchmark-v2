def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(len(int_list)):
        if i >= 68 and i <= 86:
            if int_list[i] % 2 != 0:
                sum += int_list[i]
    if sum == 0:
        return sum
    else:
        return sum