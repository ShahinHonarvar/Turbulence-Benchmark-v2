def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(filter(lambda x: list1[21:98].count(x) > 0 and list2[21:98].count(x) > 0, list1[21:98]))