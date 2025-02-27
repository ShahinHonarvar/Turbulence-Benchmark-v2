from itertools import zip_longest

def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        return set()
    identical_set = set()
    for element, other_element in zip_longest(list_a[20:31], list_b[20:31], fillvalue=False):
        if element != False and other_element != False and (element == other_element):
            identical_set.add(element)
    return identical_set