def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 80 and i <= 200 and (x in list2[80:201])])