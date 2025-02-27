def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[40:61])
    if len(relevant_characters) >= 19:
        return relevant_characters[18]
    else:
        return None