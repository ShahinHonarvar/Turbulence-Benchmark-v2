def identical_elements(list1, list2):
    if len(list1) != len(list2) or len(list1) < 10:
        return set()
    else:
        return {i for i in list1[0:10] if i in list2[0:10]}