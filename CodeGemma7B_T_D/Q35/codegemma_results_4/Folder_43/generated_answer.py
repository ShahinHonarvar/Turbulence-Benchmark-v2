def remove_repeat_chars(text):
    char_counts = {}
    for i in range(10, 28):
        if text[i] in char_counts:
            char_counts[text[i]] += 1
        else:
            char_counts[text[i]] = 1
    new_text = []
    for i in range(len(text)):
        if text[i] not in char_counts or char_counts[text[i]] == 1:
            new_text.append(text[i])
    return ''.join(new_text)