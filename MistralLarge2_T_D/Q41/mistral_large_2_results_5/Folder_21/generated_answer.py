def identical_elements(list1, list2):
    return {x for x in set(list1[639:976]) if x in set(list2[639:976])}