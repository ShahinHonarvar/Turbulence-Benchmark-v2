def remove_repeat_chars(s):
    section = s[104:802]
    counts = {}
    for char in section:
        counts[char] = counts.get(char, 0) + 1
    to_remove = {char for char, count in counts.items() if count > 1}
    result = [char for char in s if not (104 < s.index(char) < 802 and char in to_remove)]
    return ''.join(result)