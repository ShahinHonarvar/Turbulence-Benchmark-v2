def sum_even_ints_inclusive(int_list):
    start_index = 660
    end_index = 924
    sum_of_even_ints = 0
    for i in range(start_index, end_index + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum_of_even_ints += int_list[i]
    return sum_of_even_ints if sum_of_even_ints > 0 else 0