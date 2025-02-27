def remove_repeat_chars(text):
    chars_to_remove = set()
    for i in range(476, 709):
        if text.count(text[i]) > 1:
            chars_to_remove.add(text[i])
    result = ''
    for char in text:
        if char not in chars_to_remove:
            result += char
    return result