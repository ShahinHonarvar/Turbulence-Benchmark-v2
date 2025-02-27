def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[40:61])
    if len(relevant_characters) < 19:
        return None
    else:
        return relevant_characters[18]