def remove_repeat_chars(text):
    to_remove = set()
    for i in range(10, 28):
        if text.count(text[i]) > 1:
            to_remove.add(text[i])
    return ''.join([char for char in text if char not in to_remove])