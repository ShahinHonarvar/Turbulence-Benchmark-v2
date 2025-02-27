def identical_elements(list_a, list_b):
    """Returns the set of all elements that occur at least once in both lists anywhere between index 40 and index 80, both inclusive.
    If no such elements exist in the given lists, the function should return an empty set."""
    if len(list_a) != len(list_b) or len(list_a) < 40 or len(list_b) < 40:
        return set()
    set_a = set(list_a[40:81])
    set_b = set(list_b[40:81])
    return set_a.intersection(set_b)