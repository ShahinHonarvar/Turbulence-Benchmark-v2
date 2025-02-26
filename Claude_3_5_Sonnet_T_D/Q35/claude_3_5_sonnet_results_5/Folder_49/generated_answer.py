def remove_repeat_chars(s):
    if len(s) <= 91:
        return s
    start = 91
    end = min(200, len(s))
    substring = s[start:end]
    char_count = {char: substring.count(char) for char in set(substring)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove))
    return result