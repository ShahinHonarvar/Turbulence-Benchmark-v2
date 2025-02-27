def remove_repeat_chars(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    repeat_chars = [key for key, value in char_counts.items() if value > 1 and 40 <= string.index(key) < 200]
    for char in repeat_chars:
        string = string.replace(char, '')
    return string