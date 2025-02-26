def remove_repeat_chars(string):
    if len(string) <= 87:
        return string
    substring = string[82:86]
    char_counts = {}
    repeat_chars = set()
    for char in substring:
        char_counts[char] = char_counts.get(char, 0) + 1
        if char_counts[char] > 1:
            repeat_chars.add(char)
    result = ''.join((char for char in string if char not in repeat_chars))
    return result