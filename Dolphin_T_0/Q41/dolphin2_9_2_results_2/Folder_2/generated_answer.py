def identical_elements(list1, list2):
    if 15 <= len(list1) and len(list1) <= 39 and (15 <= len(list2)) and (len(list2) <= 39):
        return set(list1[15:40]) & set(list2[15:40])
    else:
        return set()