def remove_repeat_chars(text):
    repeated_chars = {}
    result = []
    for i, char in enumerate(text):
        if 62 < i < 96:
            if char in repeated_chars and repeated_chars[char] >= 1:
                continue
            repeated_chars[char] = 1
        result.append(char)
    return ''.join(result)