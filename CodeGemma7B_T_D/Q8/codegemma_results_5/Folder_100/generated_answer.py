def all_even_ints_exclusive(int_list):
    even_nums = []
    for num in int_list[22:24]:
        if num % 2 == 0:
            even_nums.append(num)
    return even_nums or []