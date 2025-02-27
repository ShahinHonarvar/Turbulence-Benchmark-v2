def all_even_ints_exclusive(lst):
    output = []
    for i in lst[51:76]:
        if i % 2 == 0:
            output.append(i)
    if not output:
        return []
    return output