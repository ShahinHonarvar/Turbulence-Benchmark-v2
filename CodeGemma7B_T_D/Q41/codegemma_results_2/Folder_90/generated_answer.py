def identical_elements(first, second):
    set1 = {val for ind, val in enumerate(first) if 262 <= ind <= 746 and val in second}
    return set1