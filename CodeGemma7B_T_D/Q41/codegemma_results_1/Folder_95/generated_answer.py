def identical_elements(list_a, list_b):
    """
    returns set of identical elements in range 82 to 86
    """
    return set([element for element in list_a[82:87] if element in list_b[82:87]])