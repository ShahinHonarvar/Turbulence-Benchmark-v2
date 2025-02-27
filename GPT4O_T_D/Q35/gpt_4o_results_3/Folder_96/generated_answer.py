def remove_repeat_chars(s):
    if not s:
        return s
    char_counts = {}
    for i in range(61, min(200, len(s))):
        char_counts[s[i]] = char_counts.get(s[i], 0) + 1
    chars_to_remove = {ch for ch, count in char_counts.items() if count > 1}
    return ''.join((ch for ch in s if ch not in chars_to_remove or s.index(ch) <= 60 or s.index(ch) >= 200))