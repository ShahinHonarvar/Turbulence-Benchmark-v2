def identical_elements(lst1, lst2):
    results = set()
    for element in lst1[43:87]:
        if element in lst2[43:87]:
            results.add(element)
    return results