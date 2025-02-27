def identical_elements(listA, listB):
    results_set = set()
    for i in range(33, 37):
        if listA[i] in listB[i]:
            results_set.add(listA[i])
    return results_set