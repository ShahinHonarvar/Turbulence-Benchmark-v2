def remove_repeat_chars(text):
    char_counts = {}
    for i in range(57, 84):
        if text[i] in char_counts:
            char_counts[text[i]] += 1
        else:
            char_counts[text[i]] = 1
    result = []
    for char in text:
        if char in char_counts and char_counts[char] == 1:
            result.append(char)
        elif char not in char_counts:
            result.append(char)
    return ''.join(result)