def return_nth_smallest_ascii(text):
    relevant_characters = sorted([ord(text[i]) for i in range(len(text)) if i <= 69])
    return chr(relevant_characters[9])