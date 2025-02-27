def identical_elements(list1, list2):
    return set([x for i, x in enumerate(list1) if i >= 40 and i <= 80 and (x in list2[40:81])])