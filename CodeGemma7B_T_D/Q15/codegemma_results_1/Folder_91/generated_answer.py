def sum_odd_ints_inclusive(num_list):
    sum = 0
    i = 0
    while i <= 5:
        if i >= 0 and i <= 5 and (num_list[i] % 2 != 0):
            sum += num_list[i]
        i += 1
    return sum