def identical_elements(list1, list2):
    return {val for val in list1[5:8] for val in list2[5:8] if val in list2[5:8]}