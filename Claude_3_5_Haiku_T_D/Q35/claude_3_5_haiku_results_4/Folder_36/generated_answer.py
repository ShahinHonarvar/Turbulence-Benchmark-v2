def remove_repeat_chars(text):
    segment = text[477:709]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    result = ''.join((char for char in text if char not in repeat_chars or text.index(char) < 477 or text.index(char) >= 709))
    return result