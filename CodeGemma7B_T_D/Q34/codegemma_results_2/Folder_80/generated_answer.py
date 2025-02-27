def find_original_set(a):
    original_set = a[0]
    for b in a:
        original_set &= b
    return original_set