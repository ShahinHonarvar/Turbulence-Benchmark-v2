def remove_repeat_chars(s: str) -> str:
    chars_between_56_and_90 = set(s[56:90])
    char_count_in_that_range = {char: s[56:90].count(char) for char in chars_between_56_and_90}
    repeated_chars = {char for char in chars_between_56_and_90 if char_count_in_that_range[char] > 1}
    result = ''.join((char for char in s[56:90] if char not in repeated_chars))
    return s[:56] + result + s[90:]