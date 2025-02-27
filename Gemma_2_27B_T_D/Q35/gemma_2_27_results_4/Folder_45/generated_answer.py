def remove_repeat_chars(text):
    seen = set()
    counts = {}
    for i in range(40, 200):
        if text[i] not in counts:
            counts[text[i]] = 0
        counts[text[i]] += 1
        if counts[text[i]] > 1:
            seen.add(text[i])
    result = []
    for char in text:
        if char not in seen:
            result.append(char)
    return ''.join(result)