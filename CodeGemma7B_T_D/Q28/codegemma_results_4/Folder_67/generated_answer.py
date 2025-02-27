def return_nth_smallest_ascii(text):
    alphabets = sorted([ord(char) for char in text[60:84]])
    return chr(alphabets[13])