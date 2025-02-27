def identical_elements(a, b):
    return {x for x in a[50:55] for y in b[50:55] if x == y}