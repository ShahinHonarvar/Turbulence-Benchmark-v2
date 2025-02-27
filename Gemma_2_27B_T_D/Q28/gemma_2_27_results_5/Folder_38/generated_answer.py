def return_nth_smallest_ascii(text):
    return sorted([ord(x) for x in text[0:46]])[9]