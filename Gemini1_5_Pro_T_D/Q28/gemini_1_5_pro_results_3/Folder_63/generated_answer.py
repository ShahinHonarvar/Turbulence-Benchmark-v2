def return_nth_smallest_ascii(text):
    relevant_characters = sorted(set(text[47:71]))
    if len(relevant_characters) >= 14:
        return relevant_characters[13]
    else:
        return None