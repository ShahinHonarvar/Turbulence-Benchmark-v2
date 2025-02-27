def sum_odd_ints_inclusive(num_list):
    sum = 0
    for i in num_list[15:39 + 1]:
        if i % 2 != 0:
            sum += i
    return sum or 0