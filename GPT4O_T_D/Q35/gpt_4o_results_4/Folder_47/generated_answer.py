def remove_repeat_chars(s):
    sub_str = s[30:53]
    counts = {}
    for char in sub_str:
        counts[char] = counts.get(char, 0) + 1
    repeat_chars = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in repeat_chars or (s.index(char) < 30 or s.index(char) >= 53)))
    return result