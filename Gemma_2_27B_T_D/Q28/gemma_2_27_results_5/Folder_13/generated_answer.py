def return_nth_smallest_ascii(text):
    relevant_chars = sorted([ord(char) for char in text[47:81] if char not in ' '])
    if len(relevant_chars) >= 4:
        return chr(relevant_chars[3])
    else:
        return ''