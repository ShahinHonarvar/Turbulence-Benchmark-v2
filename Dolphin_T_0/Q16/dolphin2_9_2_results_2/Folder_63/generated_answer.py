def sum_even_ints_inclusive(num_list):
    total = 0
    for i in range(22, 89):
        if num_list[i] % 2 == 0:
            total += num_list[i]
    return total if total != 0 else 0