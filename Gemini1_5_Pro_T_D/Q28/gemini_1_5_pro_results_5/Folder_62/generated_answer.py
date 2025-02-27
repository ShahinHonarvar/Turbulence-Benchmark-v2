def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[51:79])
    if len(relevant_characters) >= 9:
        return relevant_characters[8]
    else:
        return None