def all_even_ints_exclusive(lst):
    result = []
    for i in lst[1:3]:
        if i % 2 == 0:
            result.append(i)
    return result