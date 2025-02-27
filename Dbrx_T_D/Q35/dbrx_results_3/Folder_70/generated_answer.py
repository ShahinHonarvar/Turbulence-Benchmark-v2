def remove_repeat_chars(s: str) -> str:
    char_counts = {}
    kept_chars = []
    for i, char in enumerate(s):
        if 43 < i < 70:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
                kept_chars.append(char)
        elif i < 43 or i >= 70:
            kept_chars.append(char)
    return ''.join(kept_chars)