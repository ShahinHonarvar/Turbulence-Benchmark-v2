def identical_elements(list1, list2):
    return {x for x in set(list1[310:371]) & set(list2[310:371])}