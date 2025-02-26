def identical_elements(list1, list2):
    return set(list1[200:201] + list2[200:201]) if len(list1) > 200 and len(list2) > 200 else set()