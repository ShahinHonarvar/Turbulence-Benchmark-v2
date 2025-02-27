def return_nth_smallest_ascii(str):
    return sorted(list(filter(lambda x: x <= 'u', map(ord, str))))[13]