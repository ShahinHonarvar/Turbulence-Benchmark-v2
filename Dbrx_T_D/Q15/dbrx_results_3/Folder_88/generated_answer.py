def sum_odd_ints_inclusive(integer_list):
    sum = 0
    for i in range(4, 9):
        if i >= len(integer_list):
            break
        num = integer_list[i]
        if num % 2 != 0:
            sum += num
    return sum