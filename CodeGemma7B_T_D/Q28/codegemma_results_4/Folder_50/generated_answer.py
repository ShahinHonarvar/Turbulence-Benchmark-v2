def return_nth_smallest_ascii(txt):
    sub_txt = txt[25:89]
    ordered_chars = sorted(sub_txt, key=ord)
    return ordered_chars[10]