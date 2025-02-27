def identical_elements(list1, list2):
    return set(filter(lambda x: x in list1[40:81] and x in list2[40:81], list1[40:81] + list2[40:81]))