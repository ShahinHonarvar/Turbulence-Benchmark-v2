def return_nth_smallest_ascii(text):
    return sorted([ch for ch in text if 47 <= ord(ch) <= 80])[3]