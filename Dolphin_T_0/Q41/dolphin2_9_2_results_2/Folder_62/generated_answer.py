def identical_elements(list1, list2):
    overlapping_elements = {i for i in set(list1[91:100]) if i in list2[91:100]}
    return overlapping_elements