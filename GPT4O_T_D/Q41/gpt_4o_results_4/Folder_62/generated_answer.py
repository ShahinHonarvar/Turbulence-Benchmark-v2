def identical_elements(list1, list2):
    if len(list1) < 100 or len(list2) < 100:
        return set()
    return set(list1[91:100]) & set(list2[91:100])