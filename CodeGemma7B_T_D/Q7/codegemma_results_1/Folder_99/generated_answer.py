def all_even_ints_inclusive(int_lst):
    even_nums = []
    for num in int_lst[310:371]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums