def remove_repeat_chars(text):
    char_count = {}
    for i in range(46, 91):
        char_count[text[i]] = char_count.get(text[i], 0) + 1
    repeat_chars = [char for char, count in char_count.items() if count > 1]
    for char in repeat_chars:
        text = text.replace(char, '')
    return text