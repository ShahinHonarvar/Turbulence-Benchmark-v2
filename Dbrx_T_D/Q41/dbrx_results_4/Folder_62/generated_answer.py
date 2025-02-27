def identical_elements(list1, list2):
    return {element for element in set(list1) & set(list2) if list1[90:100].count(element) + list2[90:100].count(element) >= 1}