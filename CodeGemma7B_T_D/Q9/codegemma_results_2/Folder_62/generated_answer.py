def all_odd_ints_inclusive(int_list):
    """
    Returns a list of all odd integers from index 91 to index 99, both inclusive.
    """
    odd_ints = []
    for i in range(91, 100):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints