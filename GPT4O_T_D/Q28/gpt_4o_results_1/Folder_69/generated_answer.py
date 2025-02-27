def return_nth_smallest_ascii(s):
    target_characters = s[67:78]
    ascii_sorted_chars = sorted(target_characters, key=lambda x: ord(x))
    if len(ascii_sorted_chars) >= 7:
        return ascii_sorted_chars[6]
    return ''