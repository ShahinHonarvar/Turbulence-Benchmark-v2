def filter_chars(s):
    if len(s) <= 476:
        return s
    chars_to_remove = {chr(i) for i in range(ord('b') + 1, ord('d'))}
    filtered_part = ''.join((c for c in s[477:948] if c not in chars_to_remove))
    return s[:477] + filtered_part + s[948:]