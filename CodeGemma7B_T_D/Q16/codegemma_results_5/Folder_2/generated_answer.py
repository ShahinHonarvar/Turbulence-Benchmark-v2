def sum_even_ints_inclusive(lst):
    total_sum = 0
    for num in lst[15:40]:
        if num % 2 == 0:
            total_sum += num
    return total_sum