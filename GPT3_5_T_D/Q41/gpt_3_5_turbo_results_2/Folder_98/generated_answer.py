def identical_elements(list1, list2):
    identical = set()
    for element1 in list1[:6]:
        if element1 in list2[:6]:
            identical.add(element1)
    return identical