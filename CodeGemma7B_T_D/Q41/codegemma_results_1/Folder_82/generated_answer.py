from itertools import compress

def identical_elements(list_1, list_2):
    return set(compress(list_1, list_2)) & set(compress(list_2, list_1))