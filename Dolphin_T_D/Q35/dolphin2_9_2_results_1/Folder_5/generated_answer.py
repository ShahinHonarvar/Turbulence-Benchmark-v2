def remove_repeat_chars(text):
    counts = {}
    for i in range(2, 8):
        if text[i] in counts:
            counts[text[i]] += 1
        else:
            counts[text[i]] = 1
    result = ''
    for char in text:
        if char not in counts or counts[char] < 2:
            result += char
    return result