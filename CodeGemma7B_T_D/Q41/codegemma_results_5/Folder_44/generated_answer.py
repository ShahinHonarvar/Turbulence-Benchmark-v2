def identical_elements(list_one, list_two):
    result = set((element for element in list_one[13:69] if element in list_two[13:69]))
    return result if len(result) > 0 else set()