def remove_repeat_chars(string):
    if len(string) <= 926:
        return string
    segment = string[376:926]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    chars_to_remove = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in string if char not in chars_to_remove or string.index(char) < 376 or string.index(char) >= 926))
    return result