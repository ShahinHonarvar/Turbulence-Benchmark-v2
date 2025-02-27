def return_nth_smallest_ascii(text):
    return sorted([ord(c) for c in text[1:37]])[14]