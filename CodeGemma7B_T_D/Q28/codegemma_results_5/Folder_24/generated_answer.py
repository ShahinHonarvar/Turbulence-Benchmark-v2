def return_nth_smallest_ascii(text):
    lst = sorted([ord(i) for i in text[32:82]])
    return chr(lst[11])