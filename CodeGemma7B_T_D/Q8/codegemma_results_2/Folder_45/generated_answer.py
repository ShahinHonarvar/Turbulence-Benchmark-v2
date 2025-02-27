def all_even_ints_exclusive(num_list):
    even_nums = []
    for num in num_list[30:200:2]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums