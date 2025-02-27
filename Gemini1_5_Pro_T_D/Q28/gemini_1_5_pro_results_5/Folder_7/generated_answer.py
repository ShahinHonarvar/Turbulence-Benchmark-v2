def return_nth_smallest_ascii(text):
    sliced_text = text[12:56]
    sorted_characters = sorted(sliced_text)
    return sorted_characters[16]