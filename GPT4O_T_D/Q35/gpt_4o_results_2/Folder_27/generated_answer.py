def remove_repeat_chars(s):
    if len(s) <= 89:
        return s
    char_counts = {}
    for i in range(87, 89):
        char = s[i]
        if s.count(char, 87, 89) > 1:
            char_counts[char] = char_counts.get(char, 0) + 1
    result = [char for char in s if char not in char_counts]
    return ''.join(result)