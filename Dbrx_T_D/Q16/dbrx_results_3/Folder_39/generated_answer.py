def sum_even_ints_inclusive(int_list):
    start = 20
    end = 30
    sum = 0
    for i in range(start, end + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum