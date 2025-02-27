def sum_odd_ints_inclusive(num_list):
    sum = 0
    for num in num_list[10:67]:
        if num % 2 != 0:
            sum += num
    return sum or 0