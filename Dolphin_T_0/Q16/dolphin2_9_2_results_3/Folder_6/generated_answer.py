def sum_even_ints_inclusive(input_list):
    total = 0
    for i in range(10, 67):
        if isinstance(input_list[i], int) and input_list[i] % 2 == 0:
            total += input_list[i]
    return total if total else 0