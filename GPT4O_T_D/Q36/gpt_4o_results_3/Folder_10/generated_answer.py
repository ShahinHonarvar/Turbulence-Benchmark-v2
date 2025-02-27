def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('!') + 1, ord('B'))}
    start, end = (35, 60)
    sub_string = s[start + 1:end]
    characters_to_eliminate = {c for c in sub_string if c in chars_to_remove}
    return ''.join((c for c in s if c not in characters_to_eliminate))