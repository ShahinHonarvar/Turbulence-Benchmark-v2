def remove_repeat_chars(s):
    sub_str = s[21:36]
    repeated_chars = set()
    unique_chars = set()
    for char in sub_str:
        if char in unique_chars:
            repeated_chars.add(char)
        unique_chars.add(char)
    result = []
    for char in s:
        if char not in repeated_chars:
            result.append(char)
    return ''.join(result)