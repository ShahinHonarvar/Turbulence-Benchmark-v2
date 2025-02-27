def return_nth_smallest_ascii(string):
    relevant_characters = sorted(string[34:86])
    if len(relevant_characters) >= 20:
        return relevant_characters[19]
    else:
        return None