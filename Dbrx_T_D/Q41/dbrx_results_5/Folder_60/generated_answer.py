def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 75 or len(list1) > 85:
        return set()
    else:
        return set(list1[74:85 + 1]).intersection(set(list2[74:85 + 1]))