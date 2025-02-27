def remove_repeat_chars(s):
    chars_to_remove = {s[i]: i for i in range(10, 79) if s[i] in s[i + 1:79]}
    for char in chars_to_remove:
        s = s.replace(char, '', chars_to_remove[char] - 10)
    return s