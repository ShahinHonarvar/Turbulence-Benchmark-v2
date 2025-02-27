def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[14:67])
    if len(relevant_characters) >= 8:
        return relevant_characters[7]
    else:
        return None