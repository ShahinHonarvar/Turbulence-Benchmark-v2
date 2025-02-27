def all_even_ints_exclusive(integers):
    temp = []
    for i in range(385, 999):
        if integers[i] % 2 == 0:
            temp.append(integers[i])
    if len(temp) == 0:
        return []
    else:
        return temp