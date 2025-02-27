def return_nth_smallest_ascii(text):
    relevant_characters = text[25:89]
    sorted_characters = sorted(relevant_characters)
    return sorted_characters[10]