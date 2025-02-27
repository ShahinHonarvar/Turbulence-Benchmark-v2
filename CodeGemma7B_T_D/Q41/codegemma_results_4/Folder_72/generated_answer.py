from typing import Set

def identical_elements(list_a: list, list_b: list) -> Set:
    if len(list_a) != len(list_b) or len(list_a) < 52 or len(list_b) < 52:
        raise ValueError('Lists must be the same size and have a length of at least 52.')
    set_a = set(list_a[29:52])
    set_b = set(list_b[29:52])
    return set_a & set_b