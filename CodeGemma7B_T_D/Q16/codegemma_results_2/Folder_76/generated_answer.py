def sum_even_ints_inclusive(num_list):
    total = 0
    for i in num_list[686:988]:
        if i % 2 == 0:
            total += i
    if total == 0:
        return 0
    else:
        return total