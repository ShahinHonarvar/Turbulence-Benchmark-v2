def remove_repeat_chars(s):
    sub_str = s[40:43]
    counts = {}
    for char in sub_str:
        counts[char] = counts.get(char, 0) + 1
    chars_to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 40 or s.index(char) >= 43))
    return result