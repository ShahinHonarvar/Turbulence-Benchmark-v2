def identical_elements(l1: list, l2: list) -> set:
    if len(l1) == len(l2):
        return set([e for e in l1[75:89] if e in l2[75:89]])
    else:
        raise ValueError('Error: Lists must be same size.')