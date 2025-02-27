def return_n_smallest_chars(s):
    return sorted([x for x in s], key=lambda x: ord(x), reverse=True)[:3]