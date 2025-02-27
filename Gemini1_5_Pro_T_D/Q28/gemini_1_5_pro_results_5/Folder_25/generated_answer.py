def return_nth_smallest_ascii(string):
    relevant_characters = string[34:69]
    sorted_characters = sorted(relevant_characters)
    return sorted_characters[5]