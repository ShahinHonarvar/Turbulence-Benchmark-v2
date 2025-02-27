def all_even_ints_exclusive(lst):
    lst = lst[1:-1]
    result = []
    for i in lst:
        if i % 2 == 0:
            result.append(i)
    return result