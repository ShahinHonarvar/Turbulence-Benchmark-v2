def sum_odd_ints_inclusive(num_list):
    sum_odd = 0
    for num in num_list[0:3]:
        if num % 2 != 0:
            sum_odd += num
    if sum_odd == 0:
        return 0
    else:
        return sum_odd