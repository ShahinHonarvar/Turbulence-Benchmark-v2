def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 91 or len(list1) > 99:
        return set()
    return set(list1[90:100]).intersection(list2[90:100])