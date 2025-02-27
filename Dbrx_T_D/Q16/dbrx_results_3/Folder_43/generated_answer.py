def sum_even_ints_inclusive(int_list):
    start_index = 68
    end_index = 86
    even_sums = 0
    for i in range(start_index, end_index + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            even_sums += int_list[i]
    if even_sums == 0:
        return 'No even integers found in the specified range.'
    return even_sums