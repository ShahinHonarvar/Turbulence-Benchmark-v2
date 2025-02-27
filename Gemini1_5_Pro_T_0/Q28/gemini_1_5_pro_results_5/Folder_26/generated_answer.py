def return_nth_smallest_ascii(string):
    extracted_string = string[1:37]
    sorted_characters = sorted(extracted_string)
    return sorted_characters[14]