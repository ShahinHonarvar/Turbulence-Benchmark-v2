def sum_odd_ints_inclusive(my_list):
    sum = 0
    for i in range(30, 49):
        if i >= len(my_list):
            break
        if my_list[i] % 2 != 0:
            sum += my_list[i]
    return sum