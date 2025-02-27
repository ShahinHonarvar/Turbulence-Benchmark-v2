def return_nth_smallest_ascii(s):
    sorted_chars = sorted(s[i:j + 1])[16]
    i, j = (12, 55)
    return sorted_chars if i <= j else None