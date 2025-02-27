def return_nth_smallest_ascii(string):
    relevant_characters = sorted(string[60:89])
    if len(relevant_characters) >= 7:
        return relevant_characters[6]
    else:
        return None