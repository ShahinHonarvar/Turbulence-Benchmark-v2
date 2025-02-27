def identical_elements(list1, list2):
    return {x for x in list1[:8] if x in list2[:8]}