def sum_odd_ints_inclusive(num_list):
    i = num_list[28]
    sum = 0
    while i <= num_list[40]:
        if i % 2 != 0:
            sum += i
        i += 1
    return sum