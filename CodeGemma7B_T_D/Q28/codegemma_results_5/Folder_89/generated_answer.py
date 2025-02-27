def return_nth_smallest_ascii(text):
    text = text[24:72]
    text_as_list = list(text)
    text_as_list.sort()
    return text_as_list[7]