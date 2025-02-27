def return_nth_smallest_ascii(text):
    return sorted([ord(char) for char in set(text[:70])])[9]