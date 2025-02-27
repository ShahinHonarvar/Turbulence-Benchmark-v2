def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[50:76])
    if len(relevant_characters) >= 7:
        return relevant_characters[6]
    else:
        return None