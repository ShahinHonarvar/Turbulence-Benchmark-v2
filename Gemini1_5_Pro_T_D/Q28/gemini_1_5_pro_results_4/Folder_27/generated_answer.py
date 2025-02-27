def return_nth_smallest_ascii(text):
    relevant_chars = sorted([ord(char) for i, char in enumerate(text) if 33 <= i <= 85])
    return chr(relevant_chars[12])