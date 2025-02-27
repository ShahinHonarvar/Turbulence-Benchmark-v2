def remove_repeat_chars(text):
    char_counts = {}
    for i in range(56, 88):
        if text[i] in char_counts:
            char_counts[text[i]] += 1
        else:
            char_counts[text[i]] = 1
    result = []
    for char in text:
        if char not in char_counts or char_counts[char] == 1:
            result.append(char)
    return ''.join(result)