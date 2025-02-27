def all_even_ints_exclusive(a):
    result = []
    for element in a[3:8]:
        if element % 2 == 0:
            result.append(element)
    return result