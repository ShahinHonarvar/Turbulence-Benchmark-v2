def return_nth_smallest_ascii(text):
    substring = text[:4]
    return sorted(substring, key=ord)[3]