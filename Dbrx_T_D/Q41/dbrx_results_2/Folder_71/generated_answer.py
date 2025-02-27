def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return {e for e in set(list1[26:53]) & set(list2[26:53]) if list1.count(e) > 0 and list2.count(e) > 0}