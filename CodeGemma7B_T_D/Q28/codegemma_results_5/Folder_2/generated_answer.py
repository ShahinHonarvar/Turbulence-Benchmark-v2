def return_nth_smallest_ascii(text):
    n = 5
    seen = text[48:77]
    return min(sorted(seen), key=ord)