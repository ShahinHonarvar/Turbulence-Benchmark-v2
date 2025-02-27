def return_nth_smallest_ascii(text):
    relevant_chars = sorted([ord(char) for char in text[17:87]])
    return chr(relevant_chars[14])