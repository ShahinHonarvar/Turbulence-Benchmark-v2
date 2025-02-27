def all_even_ints_exclusive(lst):
    """ function to find and return all even integers from index 44 to index 78, both exclusive. """
    result = []
    for i in range(44, 78):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    if len(result) == 0:
        return []
    else:
        return result