def remove_repeat_chars(s):
    if len(s) <= 70:
        return s
    substr = s[70:97]
    duplicates = {char for char in substr if substr.count(char) > 1}
    return ''.join((char for char in s if char not in duplicates))