def remove_repeat_chars(text):
    counts = {}
    for char in text[200:202]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text