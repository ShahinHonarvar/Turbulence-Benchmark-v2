def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[9:60])
    if len(relevant_characters) >= 6:
        return relevant_characters[5]
    else:
        return None