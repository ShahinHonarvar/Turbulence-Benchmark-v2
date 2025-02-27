def return_nth_smallest_ascii(string):
    relevant_characters = string[62:84]
    sorted_characters = sorted(relevant_characters)
    return sorted_characters[8]