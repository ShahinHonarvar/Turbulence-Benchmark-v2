def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 30 or len(list1) > 200:
        return set()
    return {i for i in set(list1[30:201]).intersection(set(list2[30:201]))}