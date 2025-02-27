def all_even_ints_exclusive(num_list):
    if not num_list:
        return []
    filtered_list = num_list[6:9]
    even_nums = []
    for number in filtered_list:
        if number % 2 == 0 and 6 < filtered_list.index(number) < 9:
            even_nums.append(number)
    return even_nums