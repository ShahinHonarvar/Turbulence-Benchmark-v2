def return_n_greatest_chars(s):
    if len(s) < 2:
        return []
    sorted_chars = sorted(s, key=lambda x: ord(x), reverse=True)
    return sorted(sorted_chars[:2])