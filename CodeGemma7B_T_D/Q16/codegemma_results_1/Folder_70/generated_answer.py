def sum_even_ints_inclusive(num_list):
    total = 0
    simple_range = num_list[28:33]
    for num in simple_range:
        if num % 2 == 0:
            total += num
    if total == 0:
        return 0
    return total