from collections import defaultdict

def identical_elements(lst1, lst2):
    element_counts = defaultdict(int)
    for i in range(32, 36):
        element_counts[lst1[i]] += 1
        element_counts[lst2[i]] += 1
    return {element for element, count in element_counts.items() if count >= 2}