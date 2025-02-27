def return_nth_smallest_ascii(string):
    relevant_characters = sorted(set(string[1:67]))
    if len(relevant_characters) >= 8:
        return relevant_characters[7]
    else:
        return None