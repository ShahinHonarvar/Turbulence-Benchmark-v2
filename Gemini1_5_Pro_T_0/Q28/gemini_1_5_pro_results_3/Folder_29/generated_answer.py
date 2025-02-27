def return_nth_smallest_ascii(text):
    sliced_text = text[5:11]
    sorted_characters = sorted(sliced_text, key=ord)
    return sorted_characters[5]