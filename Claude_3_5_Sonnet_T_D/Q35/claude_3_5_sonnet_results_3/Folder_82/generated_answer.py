def remove_repeat_chars(s):
    if len(s) <= 31:
        return s
    start = 31
    end = min(200, len(s))
    substring = s[start:end]
    char_count = {char: substring.count(char) for char in set(substring)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = s[:start]
    for char in s[start:]:
        if char not in chars_to_remove:
            result += char
    return result