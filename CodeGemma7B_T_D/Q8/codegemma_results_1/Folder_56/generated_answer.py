def all_even_ints_exclusive(list1):
    output = []
    for i in range(7, 9):
        if list1[i] % 2 == 0:
            output.append(list1[i])
    return output