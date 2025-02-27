def remove_repeat_chars(s):
    substring = s[78:84]
    char_counts = {char: substring.count(char) for char in set(substring)}
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove))