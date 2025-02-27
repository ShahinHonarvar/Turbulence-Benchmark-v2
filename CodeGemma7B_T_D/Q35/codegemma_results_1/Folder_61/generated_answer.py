def remove_repeat_chars(text):
    unique_chars = []
    result = []
    for char in text:
        if char not in unique_chars and text.index(char) >= 0 and (text.index(char) < 8):
            unique_chars.append(char)
            result.append(char)
    return ''.join(result)