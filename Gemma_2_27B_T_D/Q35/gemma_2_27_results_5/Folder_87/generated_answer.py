def remove_repeat_chars(text):
    char_counts = {}
    for i in range(20, 43):
        if text[i] in char_counts:
            char_counts[text[i]] += 1
        else:
            char_counts[text[i]] = 1
    result = []
    for char in text:
        if char in char_counts and char_counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)