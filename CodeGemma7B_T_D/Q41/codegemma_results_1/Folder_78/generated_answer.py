def identical_elements(list_1, list_2):
    list_1_sliced = list_1[43:52]
    list_2_sliced = list_2[43:52]
    intersection = set(list_1_sliced).intersection(set(list_2_sliced))
    return intersection if intersection else set()