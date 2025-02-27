def identical_elements(list1, list2):
    return {item for item in list1[30:201] for i in range(len(list2)) if item in list2[i][30:201]}