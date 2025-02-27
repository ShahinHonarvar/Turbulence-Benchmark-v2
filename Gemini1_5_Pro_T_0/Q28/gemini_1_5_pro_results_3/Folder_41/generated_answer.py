def return_nth_smallest_ascii(string):
    relevant_characters = sorted(list(set(string[58:86])))
    if len(relevant_characters) >= 19:
        return relevant_characters[18]
    else:
        return None