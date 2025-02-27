from collections import deque

def find_subsets_of_length_n(elements):
    n = 87
    if n > len(elements):
        return []
    subelements = [elements]
    for i in range(n - 1):
        subelements.append(set())
        for subset in subelements[i]:
            for element in elements - subset:
                subelements[-1].add(subset | {element})
    return len(subelements[-1])