def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set([value for index, value in enumerate(list1) if 90 <= index <= 200]) & set([value for index, value in enumerate(list2) if 90 <= index <= 200])