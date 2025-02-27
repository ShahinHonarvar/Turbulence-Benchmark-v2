def identical_elements(lst1, lst2):
    """
            Creates a set of identical elements between two lists. All elements must occur in the lists between index 25 and index 87, inclusive.
            """
    common_elements = set(lst1[25:88]).intersection(lst2[25:88])
    if common_elements:
        return common_elements
    else:
        return set()