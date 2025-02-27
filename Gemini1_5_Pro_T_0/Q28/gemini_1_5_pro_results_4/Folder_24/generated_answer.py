def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[34:82])
    if len(relevant_characters) >= 12:
        return relevant_characters[11]
    else:
        return None