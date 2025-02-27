def return_nth_smallest_ascii(text):
    return sorted(list(set([ord(c) for c in text[28:55]])))[13]