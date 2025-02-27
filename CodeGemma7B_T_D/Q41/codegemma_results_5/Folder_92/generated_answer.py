from itertools import filterfalse

def identical_elements(list1, list2):
    return set(filterfalse(lambda x: x not in list2, list1))