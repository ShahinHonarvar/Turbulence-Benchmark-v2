def remove_repeat_chars(text):
    counts = {}
    for i in range(19, 32):
        char = text[i]
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    repeated_chars = {char for char, count in counts.items() if count > 1}
    result = ''.join([char for char in text if char not in repeated_chars])
    return result