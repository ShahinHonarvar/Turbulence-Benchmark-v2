def return_nth_smallest_ascii(txt):
    return sorted([ch for ch in txt[18:67] if ch.isalpha()], key=ord)[18]