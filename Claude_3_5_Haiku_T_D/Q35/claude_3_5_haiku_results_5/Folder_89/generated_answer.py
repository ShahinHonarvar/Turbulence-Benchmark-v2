def remove_repeat_chars(s):
    if len(s) <= 55:
        return s
    substr = s[56:84]
    seen_chars = {}
    for char in substr:
        if char in seen_chars:
            seen_chars[char] += 1
        else:
            seen_chars[char] = 1
    repeat_chars = {char for char, count in seen_chars.items() if count > 1}
    result = [char for char in s if char not in repeat_chars or s.index(char) < 56 or s.index(char) >= 84]
    return ''.join(result)