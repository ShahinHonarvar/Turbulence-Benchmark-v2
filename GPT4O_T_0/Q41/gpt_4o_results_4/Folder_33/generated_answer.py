def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 775:
        return set()
    return set(list1[667:775]).intersection(list2[667:775])