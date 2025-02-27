def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[14:36])
    if len(relevant_characters) >= 11:
        return relevant_characters[10]
    else:
        return None