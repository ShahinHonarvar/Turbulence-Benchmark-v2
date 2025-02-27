from itertools import compress

def identical_elements(lst1, lst2):
    lst1 = lst1[56:58]
    lst2 = lst2[56:58]
    return set(compress(lst1, lst2))