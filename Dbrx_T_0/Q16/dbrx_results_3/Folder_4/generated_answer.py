def sum_even_ints_inclusive(int_list):
    start_index = 12
    end_index = 92
    sum = 0
    for i in range(min(start_index, len(int_list)), min(end_index + 1, len(int_list))):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum if sum > 0 else 0