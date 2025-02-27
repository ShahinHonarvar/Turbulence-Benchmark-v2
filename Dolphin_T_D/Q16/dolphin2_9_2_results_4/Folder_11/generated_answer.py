def sum_even_ints_inclusive(lst):
    sub_lst = lst[37:52]
    even_sum = 0
    for num in sub_lst:
        if num % 2 == 0:
            even_sum += num
    return even_sum or 0