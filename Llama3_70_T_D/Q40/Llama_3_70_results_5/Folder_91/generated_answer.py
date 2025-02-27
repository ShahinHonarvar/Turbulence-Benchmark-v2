def return_n_smallest_chars(s):
    return sorted(s, key=lambda x: (x not in s[:6], x), reverse=True)[:6]