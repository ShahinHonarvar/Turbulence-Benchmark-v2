def remove_repeat_chars(text):
    counts = {}
    for i in range(1, 7):
        if text[i] in counts:
            counts[text[i]] += 1
        else:
            counts[text[i]] = 1
    result = []
    for char in text:
        if char not in counts or counts[char] == 1:
            result.append(char)
    return ''.join(result)