def return_nth_smallest_ascii(s):
    chars = list(s)
    sorted_chars = sorted([ch for ch in chars[1:37] if ch.isalpha()], key=lambda ch: ord(ch))
    return sorted_chars[14]