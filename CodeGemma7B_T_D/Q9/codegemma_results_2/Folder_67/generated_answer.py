def all_odd_ints_inclusive(int_list):
    """ Write Python code to fulfill the text specification here. """
    even_list = []
    for i in range(22, 51):
        if i % 2 != 0:
            even_list.append(i)
    return even_list