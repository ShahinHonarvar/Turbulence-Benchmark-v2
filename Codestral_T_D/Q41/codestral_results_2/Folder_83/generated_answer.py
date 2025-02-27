def identical_elements(list1, list2):
    start, end = (90, 200)
    return set(list1[start:end + 1]) & set(list2[start:end + 1])