def sum_odd_ints_inclusive(int_list):
    sum = 0
    for num in int_list[0:8]:
        if num % 2 != 0:
            sum += num
    if sum == 0:
        return 0
    else:
        return sum