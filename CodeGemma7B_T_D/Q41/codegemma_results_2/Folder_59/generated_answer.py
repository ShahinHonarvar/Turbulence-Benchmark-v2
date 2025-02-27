from itertools import filterfalse

def identical_elements(l1: list, l2: list) -> set:
    filtered_l1 = filterfalse(lambda x: x not in l2, l1)
    filtered_l2 = filterfalse(lambda x: x not in l1, l2)
    return set(filtered_l1).intersection(filtered_l2)