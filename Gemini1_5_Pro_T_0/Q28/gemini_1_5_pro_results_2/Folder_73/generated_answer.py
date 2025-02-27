def return_nth_smallest_ascii(text):
    relevant_characters = sorted(text[:70])
    if len(relevant_characters) >= 10:
        return relevant_characters[9]
    else:
        return None