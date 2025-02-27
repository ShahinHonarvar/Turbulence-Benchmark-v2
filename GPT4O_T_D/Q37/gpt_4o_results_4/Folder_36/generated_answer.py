def filter_chars(s):
    if len(s) <= 259:
        return s
    filtered_part = s[259:503]
    chars_to_remove = {chr(i) for i in range(ord(','), ord('4'))}
    result = ''.join((c for c in filtered_part if c not in chars_to_remove))
    return s[:259] + result + s[503:]