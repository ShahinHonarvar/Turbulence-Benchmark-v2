def sum_even_ints_inclusive(int_list):
    total = 0
    for num in int_list[70:85]:
        if num % 2 == 0:
            total += num
    if total == 0:
        return 0
    return total