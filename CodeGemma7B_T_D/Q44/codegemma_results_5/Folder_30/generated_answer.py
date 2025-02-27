def composite_nums_between_indices(list_integers):
    composites = set()
    for i in range(19, 93):
        if list_integers[i] % 2 == 0 or list_integers[i] % 3 == 0:
            composites.add(list_integers[i])
    returncomposites