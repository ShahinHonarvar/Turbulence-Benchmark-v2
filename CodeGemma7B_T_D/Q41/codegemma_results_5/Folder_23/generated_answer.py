def identical_elements(list1, list2):
    set_intersection = set(list1[52:72]).intersection(list2[52:72])
    if len(set_intersection) == 0:
        return set()
    else:
        return set_intersection