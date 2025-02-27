def sum_even_ints_inclusive(int_list):
    start_index = 22
    end_index = 88
    sum = 0
    if start_index < 0 or end_index > len(int_list) - 1:
        return 0
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum