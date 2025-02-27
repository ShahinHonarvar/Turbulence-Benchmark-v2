import itertools

def identical_elements(list1, list2):
    return set(itertools.compress(list1, list2)) & set(range(50, 201))