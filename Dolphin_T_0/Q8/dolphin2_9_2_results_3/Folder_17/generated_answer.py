def all_even_ints_exclusive(lst):
    even_nums = []
    for num in lst[63:96]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums