def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 70 or len(list1) > 200 or (len(list2) < 70) or (len(list2) > 200):
        return set()
    return set(list1[70:201]).intersection(list2[70:201])