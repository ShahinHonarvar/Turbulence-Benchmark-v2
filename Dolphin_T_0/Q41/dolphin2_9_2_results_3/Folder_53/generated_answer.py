def identical_elements(list1, list2):
    intersection = set(list1) & set(list2)
    return set(filter(lambda x: 200 <= list1.index(x) <= 200 and 200 <= list2.index(x) <= 200, intersection))