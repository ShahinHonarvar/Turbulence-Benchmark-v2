def sum_even_ints_inclusive(int_list):
    start_index = 22
    end_index = 63
    even_sums = 0
    if start_index < 0 or end_index >= len(int_list):
        raise IndexError('Invalid index range')
    for i in range(start_index, end_index + 1):
        if int_list[i] % 2 == 0:
            even_sums += int_list[i]
    return even_sums