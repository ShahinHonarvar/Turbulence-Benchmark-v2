def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 209 or len(list1) > 556:
        return set()
    else:
        return set(filter(lambda x: list1.count(x) > 0 and list2.count(x) > 0, list1[209:557]))