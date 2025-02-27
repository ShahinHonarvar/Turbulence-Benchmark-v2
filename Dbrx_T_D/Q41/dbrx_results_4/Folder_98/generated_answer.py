def identical_elements(list1, list2):
    if len(list1) > 5 or len(list2) > 5 or len(list1) != len(list2):
        return set()
    intersection = set(list1) & set(list2)
    trimmed_intersection = set(filter(lambda x: list1.index(x) <= 5 and list2.index(x) <= 5, intersection))
    return trimmed_intersection