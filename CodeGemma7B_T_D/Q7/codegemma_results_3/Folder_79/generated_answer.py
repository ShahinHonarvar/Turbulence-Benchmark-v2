def all_even_ints_inclusive(num_list):
    range_even_nums = []
    for num in num_list:
        if num % 2 == 0 and num in range(4, 5):
            range_even_nums.append(num)
    return range_even_nums