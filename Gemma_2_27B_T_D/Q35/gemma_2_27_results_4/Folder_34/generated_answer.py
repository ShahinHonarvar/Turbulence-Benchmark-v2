def remove_repeat_chars(text):
    char_counts = {}
    for i in range(70, 200):
        if i < len(text):
            char = text[i]
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text