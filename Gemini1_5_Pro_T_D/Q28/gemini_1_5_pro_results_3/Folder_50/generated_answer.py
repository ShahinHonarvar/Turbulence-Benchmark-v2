def return_nth_smallest_ascii(string):
    relevant_characters = sorted(string[25:89])
    if len(relevant_characters) >= 11:
        return relevant_characters[10]
    else:
        return None