def remove_repeat_chars(text):
    char_counts = {}
    for char in text[0:10]:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    result = []
    for char in text:
        if char in char_counts and char_counts[char] > 1:
            continue
        result.append(char)
    return ''.join(result)