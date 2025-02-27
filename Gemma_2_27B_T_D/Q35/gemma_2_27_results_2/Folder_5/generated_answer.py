def remove_repeat_chars(text):
    counts = {}
    for char in text[2:8]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    result = []
    for char in text:
        if char not in counts or counts[char] == 1:
            result.append(char)
    return ''.join(result)