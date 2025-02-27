def sum_odd_ints_inclusive(int_list):
    sum = 0
    for i in range(26, 53):
        if i in range(26, 53) and int_list[i] % 2 != 0:
            sum += int_list[i]
    return sum if sum > 0 else 0