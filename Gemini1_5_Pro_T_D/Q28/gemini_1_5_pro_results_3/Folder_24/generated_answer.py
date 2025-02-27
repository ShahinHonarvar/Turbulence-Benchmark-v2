def return_nth_smallest_ascii(string):
    relevant_characters = string[34:82]
    sorted_characters = sorted(relevant_characters, key=ord)
    return sorted_characters[11]