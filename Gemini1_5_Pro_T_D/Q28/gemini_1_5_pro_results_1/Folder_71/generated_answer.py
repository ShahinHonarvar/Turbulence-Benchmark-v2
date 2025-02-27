def return_nth_smallest_ascii(text):
    sliced_text = text[5:83]
    sorted_ascii = sorted(list(sliced_text), key=ord)
    return sorted_ascii[15]