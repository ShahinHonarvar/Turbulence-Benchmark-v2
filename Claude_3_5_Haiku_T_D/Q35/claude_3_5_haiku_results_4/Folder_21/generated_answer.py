def remove_repeat_chars(s):
    if len(s) <= 462:
        return s
    segment = s[463:995]
    char_counts = {}
    for char in segment:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeat_chars = {char for char, count in char_counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeat_chars or s.index(char) >= 995))