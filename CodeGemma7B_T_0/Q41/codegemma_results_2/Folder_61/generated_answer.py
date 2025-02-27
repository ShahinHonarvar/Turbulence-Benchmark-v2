def identical_elements(list1, list2):
    return set([item for item in list1 for i in range(len(list1)) if list1.index(item) in range(0, 7) and list2.index(item) in range(0, 7)])