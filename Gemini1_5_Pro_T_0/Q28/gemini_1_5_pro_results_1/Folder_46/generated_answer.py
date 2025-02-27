def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[34:86])
    if len(relevant_characters) >= 20:
        return relevant_characters[19]
    else:
        return None