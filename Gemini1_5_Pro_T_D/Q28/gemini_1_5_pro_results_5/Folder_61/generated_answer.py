def return_nth_smallest_ascii(string):
    relevant_characters = sorted(string[0:10])
    if len(relevant_characters) >= 10:
        return relevant_characters[9]
    else:
        return None