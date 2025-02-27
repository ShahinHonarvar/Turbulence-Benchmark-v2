def remove_repeat_chars(s):
    substring = s[47:91]
    char_count = {c: substring.count(c) for c in set(substring)}
    chars_to_remove = {c for c, count in char_count.items() if count > 1}
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result