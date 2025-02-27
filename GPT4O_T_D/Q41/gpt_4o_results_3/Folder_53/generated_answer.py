def identical_elements(list1, list2):
    if len(list1) >= 201 and len(list2) >= 201:
        return {list1[200]} if list1[200] == list2[200] else set()
    else:
        return set()