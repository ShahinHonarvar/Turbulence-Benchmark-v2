def identical_elements(list1, list2):
    return {item for sublist in zip(list1, list2) for item in sublist if 0 <= sublist.index(item) <= 2}