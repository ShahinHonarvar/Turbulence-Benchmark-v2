def remove_repeat_chars(text):
    counts = {}
    for i in range(20, 93):
        char = text[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    for char, count in counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text