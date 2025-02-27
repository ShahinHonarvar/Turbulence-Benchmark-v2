def return_nth_smallest_ascii(text):
    relevant_characters = sorted(set(text[25:46]))
    if len(relevant_characters) < 11:
        return None
    else:
        return relevant_characters[10]