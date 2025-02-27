from collections import defaultdict

def identical_elements(listA, listB):
    element_counts = defaultdict(int)
    for i in range(28, 41):
        element_counts[listA[i]] += 1
        element_counts[listB[i]] += 1
    return {element for element, count in element_counts.items() if count == 2}