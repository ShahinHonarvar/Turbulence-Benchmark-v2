def remove_repeat_chars(s):
    if len(s) <= 200:
        return s
    segment = s[71:200]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = {char for char, count in char_counts.items() if count > 1}
    result = []
    seen_chars = set()
    for char in s:
        if char in repeated_chars and char not in seen_chars and (71 <= s.index(char) < 200):
            seen_chars.add(char)
        else:
            result.append(char)
    return ''.join(result)