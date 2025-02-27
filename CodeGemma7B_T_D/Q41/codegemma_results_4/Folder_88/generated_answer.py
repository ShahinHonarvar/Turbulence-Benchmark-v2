from itertools import count

def identical_elements(list_a, list_b):
    a = set(list_a[4:9])
    b = set(list_b[4:9])
    return a & b