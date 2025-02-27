def identical_elements(list_a, list_b):
    return set([a for i, (a, b) in enumerate(zip(list_a[209:557], list_b[209:557])) if a == b])