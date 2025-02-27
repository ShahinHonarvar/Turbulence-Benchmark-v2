def all_even_ints_exclusive(list):
    """
            Returns a list of all even integers from index 80 to index 200, both exclusive.
            """
    even_ints = []
    for i in range(80, 200):
        if list[i] % 2 == 0:
            even_ints.append(list[i])
    return even_ints