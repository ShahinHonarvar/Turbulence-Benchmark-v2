def sum_even_ints_inclusive(int_list):
    total = 0
    for count, num in enumerate(int_list):
        if count in range(6, 9):
            if num % 2 == 0:
                total += num
    if total == 0:
        return 0
    return total