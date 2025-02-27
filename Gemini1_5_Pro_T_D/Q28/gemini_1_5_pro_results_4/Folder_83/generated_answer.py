def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[30:71])
    if len(relevant_characters) >= 15:
        return relevant_characters[14]
    else:
        return None