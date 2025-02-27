def identical_elements(list1, list2):
    start = max(42, 0)
    end = min(68, len(list1), len(list2))
    return set(list1[start:end + 1]) & set(list2[start:end + 1])