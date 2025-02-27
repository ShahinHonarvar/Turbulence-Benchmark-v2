def identical_elements(list1, list2):
    set1 = {element for index, element in enumerate(list1) if 21 <= index <= 97}
    set2 = {element for index, element in enumerate(list2) if 21 <= index <= 97}
    return set1 & set2