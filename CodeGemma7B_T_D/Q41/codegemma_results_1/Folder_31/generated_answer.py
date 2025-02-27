def identical_elements(arr1, arr2):
    sublist1 = arr1[75:89]
    sublist2 = arr2[75:89]
    intersection = set(sublist1).intersection(sublist2)
    return intersection or set()