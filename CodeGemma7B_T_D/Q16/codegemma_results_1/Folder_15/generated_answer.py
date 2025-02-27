def sum_even_ints_inclusive(num_list):
    sum_of_even_ints = 0
    max_index = min(4, len(num_list) - 1)
    for i in range(max_index + 1):
        if num_list[i] % 2 == 0:
            sum_of_even_ints += num_list[i]
    return sum_of_even_ints