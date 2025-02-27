def identical_elements(list1, list2):
    start = max(0, 43)
    end = min(len(list1), 52)
    set1 = set(list1[start:end])
    set2 = set(list2[start:end])
    return set1 & set2