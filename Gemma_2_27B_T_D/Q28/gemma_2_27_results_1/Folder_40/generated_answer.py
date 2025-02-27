def return_nth_smallest_ascii(text):
    return chr(sorted([ord(char) for char in text[:5]])[4])