def identical_elements(list1, list2):
    if len(list1) < 85 or len(list2) < 85:
        return set()
    return set(list1[70:85]).intersection(list2[70:85])