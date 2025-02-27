def sum_even_ints_inclusive(int_list):
    start_index = 52
    end_index = 71
    sum = 0
    for i in range(min(start_index, end_index), max(start_index, end_index) + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum