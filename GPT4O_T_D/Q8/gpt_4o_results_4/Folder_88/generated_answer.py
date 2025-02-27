def all_even_ints_exclusive(lst):
    result = []
    for i in lst[3:8]:
        if i % 2 == 0:
            result.append(i)
    return result