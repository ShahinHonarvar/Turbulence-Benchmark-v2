def remove_repeat_chars(text):
    char_counts = {}
    for char in text[44:91]:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = []
    for char in text:
        if char not in char_counts or char_counts[char] == 1:
            result.append(char)
        else:
            char_counts[char] -= 1
    return ''.join(result)