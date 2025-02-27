def identical_elements(list1, list2):
    return set([element for i, element in enumerate(list1[21:98]) if element in list2[21:98]])