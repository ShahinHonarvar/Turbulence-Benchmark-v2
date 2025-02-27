from collections import defaultdict

def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b) or len(list_a) < 51 or len(list_b) < 51:
        raise ValueError('Lists must be of equal length and contain at least 51 elements.')
    seen_elements = defaultdict(set)
    result = set()
    for i in range(29, 52):
        seen_elements[list_a[i]].add(list_b[i])
        if list_b[i] in seen_elements[list_a[i]]:
            result.add(list_a[i])
    return result