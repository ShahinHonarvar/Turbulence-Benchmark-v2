def all_even_ints_exclusive(lst):
    even_list = []
    for item in lst[0:10]:
        if item % 2 == 0 and item in lst[0:10]:
            even_list.append(item)
    return even_list