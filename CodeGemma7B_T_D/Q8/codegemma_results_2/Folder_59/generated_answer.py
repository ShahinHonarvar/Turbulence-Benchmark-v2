def all_even_ints_exclusive(num_list):
    even_nums = []
    for num in range(10):
        if num % 2 == 0 and num != 0 and (num in num_list):
            even_nums.append(num)
    return even_nums