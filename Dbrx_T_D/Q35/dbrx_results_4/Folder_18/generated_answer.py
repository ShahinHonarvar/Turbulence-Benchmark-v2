def remove_repeat_chars(s: str) -> str:
    chars_between_56_and_90 = set(s[56:90])
    char_count = {char: s[:56].count(char) + s[90:].count(char) for char in chars_between_56_and_90}
    return ''.join((char for char in s if char not in chars_between_56_and_90 or char_count[char] <= 1))