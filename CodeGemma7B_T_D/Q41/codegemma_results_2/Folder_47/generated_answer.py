def identical_elements(lst1, lst2):
    filtered_lst1 = [element for i, element in enumerate(lst1) if 37 <= i <= 76]
    filtered_lst2 = [element for i, element in enumerate(lst2) if 37 <= i <= 76]
    intersection = set(filtered_lst1).intersection(set(filtered_lst2))
    return intersection if intersection else set()