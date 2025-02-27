def return_nth_smallest_ascii(string):
    relevant_characters = string[10:74]
    sorted_characters = sorted(relevant_characters)
    return sorted_characters[8]