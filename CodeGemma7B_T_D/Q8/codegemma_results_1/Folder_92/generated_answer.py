def all_even_ints_exclusive(num_list: list) -> list:
    even_nums = []
    for num in num_list:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums