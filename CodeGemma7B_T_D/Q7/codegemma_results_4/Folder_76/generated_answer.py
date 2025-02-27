def all_even_ints_inclusive(numlist):
    even_list = []
    for i in range(686, 988):
        if numlist[i] % 2 == 0:
            even_list.append(numlist[i])
    return even_list