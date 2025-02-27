def return_nth_smallest_ascii(string):
    relevant_characters = sorted(string[30:71])
    if len(relevant_characters) >= 15:
        return relevant_characters[14]
    else:
        return None