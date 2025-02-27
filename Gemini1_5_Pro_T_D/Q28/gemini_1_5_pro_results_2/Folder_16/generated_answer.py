def return_nth_smallest_ascii(text):
    extracted_characters = sorted(text[18:46])
    if len(extracted_characters) >= 7:
        return extracted_characters[6]
    else:
        return None