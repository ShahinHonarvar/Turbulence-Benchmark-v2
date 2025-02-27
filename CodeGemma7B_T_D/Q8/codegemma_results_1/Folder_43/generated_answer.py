def all_even_ints_exclusive(list_of_ints):
    even_ints_in_range = []
    for num in list_of_ints[38:77]:
        if num % 2 == 0:
            even_ints_in_range.append(num)
    return even_ints_in_range