def identical_elements(list_a=None, list_b=None):
    """
            Returns the set of all elements that occur at least once in both lists anywhere between index 56 and index 98, both inclusive.
            """
    list_a = list_a or []
    list_b = list_b or []
    if not (list_a and list_b):
        raise ValueError('Both lists must be provided')
    if len(list_a) != len(list_b):
        raise ValueError('Both lists must be of the same length')
    elements_in_both = set()
    for i in range(56, 99):
        if list_a[i] == list_b[i]:
            elements_in_both.add(list_a[i])
    return elements_in_both