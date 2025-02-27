def all_even_ints_inclusive(lst):
    inclusive_list = []
    for i in range(667, 775):
        if lst[i] % 2 == 0:
            inclusive_list.append(lst[i])
    return inclusive_list