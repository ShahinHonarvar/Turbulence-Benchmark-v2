def remove_repeat_chars(text):
    counts = {}
    for i in range(35, 64):
        if text[i] in counts:
            counts[text[i]] += 1
        else:
            counts[text[i]] = 1
    result = []
    for c in text:
        if c not in counts or counts[c] == 1:
            result.append(c)
    return ''.join(result)