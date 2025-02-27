def return_n_smallest_chars(text):
    list.sort([ord(i) for i in text[:45]])
    return [chr(i) for i in list]