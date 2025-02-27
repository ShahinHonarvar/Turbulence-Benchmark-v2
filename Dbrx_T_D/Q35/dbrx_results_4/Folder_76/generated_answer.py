def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    chars_to_remove = set()
    for i in range(330, 543):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
            if char_counts[s[i]] > 1:
                chars_to_remove.add(s[i])
        else:
            char_counts[s[i]] = 1
    result = ''
    for char in s:
        if char not in chars_to_remove:
            result += char
    return result