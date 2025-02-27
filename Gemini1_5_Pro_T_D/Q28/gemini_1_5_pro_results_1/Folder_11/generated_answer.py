def return_nth_smallest_ascii(string):
    relevant_characters = sorted(string[9:60])
    if len(relevant_characters) < 6:
        return None
    else:
        return relevant_characters[5]