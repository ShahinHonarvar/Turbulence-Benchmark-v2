def identical_elements(list_a, list_b):
    same_elements = set((a for a, b in zip(list_a[91:99], list_b[91:99]) if a == b))
    return same_elements or set()