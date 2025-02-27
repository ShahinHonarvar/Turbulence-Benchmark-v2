def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[12:56])
    if len(relevant_characters) >= 17:
        return relevant_characters[16]
    else:
        return None