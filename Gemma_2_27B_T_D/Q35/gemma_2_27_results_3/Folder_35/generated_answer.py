def remove_repeat_chars(text):
    counts = {}
    for i in range(77, 84):
        if i < len(text):
            if text[i] in counts:
                counts[text[i]] += 1
            else:
                counts[text[i]] = 1
    for char, count in counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text