def all_even_ints_exclusive(num_list):
    even_nums = []
    for num in num_list[81:87]:
        if num % 2 == 0:
            even_nums.append(num)
    if not even_nums:
        return []
    return even_nums