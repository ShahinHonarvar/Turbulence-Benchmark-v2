def remove_repeat_chars(s):
    substring = s[376:926]
    char_count = {char: substring.count(char) for char in set(substring)}
    chars_to_remove = {char for char, count in char_count.items() if count > 1}
    result = [char for char in s if char not in chars_to_remove or s.index(char) <= 375 or s.index(char) >= 926]
    return ''.join(result)