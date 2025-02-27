def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[10:74])
    if len(relevant_characters) >= 9:
        return relevant_characters[8]
    else:
        return None