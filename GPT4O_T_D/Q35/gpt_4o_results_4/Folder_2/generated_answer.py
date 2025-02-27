def remove_repeat_chars(s):
    sub_str = s[73:93]
    counts = {}
    for char in sub_str:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove or s.index(char) <= 72 or s.index(char) >= 93))
    return result