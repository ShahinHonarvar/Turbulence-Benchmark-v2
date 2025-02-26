def remove_repeat_chars(s):
    if len(s) <= 78:
        return s
    target_substring = s[77:84]
    repeat_chars = set((char for char in target_substring if target_substring.count(char) > 1))
    result = ''
    for i, char in enumerate(s):
        if i < 77 or i >= 84:
            result += char
        elif char not in repeat_chars:
            result += char
    return result