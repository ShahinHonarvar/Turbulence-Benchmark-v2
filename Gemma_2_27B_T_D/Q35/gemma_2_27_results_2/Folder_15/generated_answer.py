def remove_repeat_chars(text):
    counts = {}
    for i in range(len(text)):
        if i >= 0 and i < 4:
            if text[i] in counts:
                counts[text[i]] += 1
            else:
                counts[text[i]] = 1
    result = []
    for char in text:
        if char in counts and counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)