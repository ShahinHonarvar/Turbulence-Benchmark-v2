def identical_elements(list1, list2):
    common_elements = set((item for item in list1[31:35] if item in list2[31:35]))
    return common_elements or set()