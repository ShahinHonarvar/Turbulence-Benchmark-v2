def sum_even_ints_inclusive(lst):
    even_sum = 0
    for num in lst[66:94]:
        if num % 2 == 0:
            even_sum += num
    return even_sum