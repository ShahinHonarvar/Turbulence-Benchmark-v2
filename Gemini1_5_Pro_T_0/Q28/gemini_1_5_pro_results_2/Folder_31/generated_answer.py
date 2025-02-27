def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[10:83])
    if len(relevant_characters) >= 18:
        return relevant_characters[17]
    else:
        return None