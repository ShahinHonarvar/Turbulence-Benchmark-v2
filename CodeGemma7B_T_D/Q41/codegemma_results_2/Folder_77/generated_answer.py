def identical_elements(list1, list2):
    both_lists = set((item for item in list1[527:539] if item in list2[527:539]))
    return both_lists if both_lists else set()