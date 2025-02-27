def remove_repeat_chars(text):
    count = {}
    for i in range(69, 97):
        if i < len(text):
            count[text[i]] = count.get(text[i], 0) + 1
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in text if char not in to_remove))