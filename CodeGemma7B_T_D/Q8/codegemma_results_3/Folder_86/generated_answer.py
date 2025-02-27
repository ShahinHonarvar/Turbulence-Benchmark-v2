def all_even_ints_exclusive(list_of_ints):
    even = []
    for i in list_of_ints[18:60]:
        if i % 2 == 0:
            even.append(i)
    return even