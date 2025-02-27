def identical_elements(a_list, b_list):
    """Given two lists of the same size, returns the set of all elements that occur at least once in both lists anywhere between index 12 and index 92, both inclusive. If no such elements exist in the given lists, the function should return an empty set."""
    if len(a_list) != len(b_list):
        raise ValueError('Input lists must be of the same size')
    if not 12 <= len(a_list) <= 92:
        raise ValueError('List length must be between 12 and 92')
    return {elem for elem in a_list[12:93] if elem in b_list[12:93]}