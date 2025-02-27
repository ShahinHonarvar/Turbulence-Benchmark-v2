def identical_elements(list1, list2):
    if len(list1) != len(list2):
        return set()
    return set(list(filter(lambda x: list1.index(x) in range(310, 371) and list2.index(x) in range(310, 371), list1)))