def identical_elements(list1, list2):
    if len(list1) < 86 or len(list2) < 86:
        return set()
    return set(list1[75:86]).intersection(list2[75:86])