def identical_elements(lst1: list, lst2: list) -> set:
    common_elements = set()
    for i in range(310, 371):
        if i < len(lst1) and i < len(lst2) and (lst1[i] == lst2[i]):
            common_elements.add(lst1[i])
    return common_elements