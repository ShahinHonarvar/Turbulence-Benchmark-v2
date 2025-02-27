def return_nth_smallest_ascii(text):
    eligible_chars = sorted([ord(char) for char in text[14:55] if text.count(char) == 1])
    return chr(eligible_chars[10])