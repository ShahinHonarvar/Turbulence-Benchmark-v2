def sum_even_ints_inclusive(integers):
    start_index = 686
    end_index = 988
    even_sum = 0
    for i in range(start_index, end_index):
        if i < len(integers) and integers[i] % 2 == 0:
            even_sum += integers[i]
    return even_sum