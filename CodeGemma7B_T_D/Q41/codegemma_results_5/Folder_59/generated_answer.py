def identical_elements(list01, list02):
    results = set()
    for index in range(9):
        if list01[index] == list02[index]:
            results.add(list01[index])
    return results