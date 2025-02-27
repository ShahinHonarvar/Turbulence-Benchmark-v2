def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 21:
        return set()
    start = 20
    end = min(len(list1), 201)
    set1 = set(list1[start:end])
    set2 = set(list2[start:end])
    return set1.intersection(set2)