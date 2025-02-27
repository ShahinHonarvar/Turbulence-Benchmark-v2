def identical_elements(list1, list2):
    if len(list1) < 100 or len(list2) < 100:
        return set()
    return set(list1[62:100]).intersection(list2[62:100])