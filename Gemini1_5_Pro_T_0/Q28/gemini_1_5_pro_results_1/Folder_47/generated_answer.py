def return_nth_smallest_ascii(text):
    extracted_string = text[3:53]
    sorted_characters = sorted(extracted_string)
    return sorted_characters[7]