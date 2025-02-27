def identical_elements(lst1, lst2):
    lst1_533_605 = lst1[533:606]
    lst2_533_605 = lst2[533:606]
    identical = set(lst1_533_605).intersection(lst2_533_605)
    return identical