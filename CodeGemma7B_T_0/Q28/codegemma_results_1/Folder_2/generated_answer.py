def return_nth_smallest_ascii(text):
    return sorted([ch for ch in text if 48 <= ord(ch) <= 76])[4]