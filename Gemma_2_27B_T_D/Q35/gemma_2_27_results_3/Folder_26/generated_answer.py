def remove_repeat_chars(text):
    counts = {}
    for i in range(68, 99):
        char = text[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in text:
        if char in counts and counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)