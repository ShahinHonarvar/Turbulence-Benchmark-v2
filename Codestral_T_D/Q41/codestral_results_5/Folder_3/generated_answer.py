def identical_elements(list1, list2):
    start = 62
    end = 92
    set1 = set(list1[start:end + 1])
    set2 = set(list2[start:end + 1])
    return set1 & set2