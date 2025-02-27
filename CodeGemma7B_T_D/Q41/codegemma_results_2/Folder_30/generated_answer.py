from itertools import count

def identical_elements(list1, list2):
    for i in range(55, 99):
        if any((list1[i] == x for x in list2[i])):
            return set.intersection(set(list1[55:99]), set(list2[55:99]))
    return set()