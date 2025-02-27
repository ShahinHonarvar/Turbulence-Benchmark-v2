def remove_repeat_chars(s):
    counts = {}
    for i in range(13, 70):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    chars_to_remove = []
    for char in counts:
        if counts[char] > 1:
            chars_to_remove.append(char)
    new_s = ''
    for char in s:
        if char not in chars_to_remove:
            new_s += char
    return new_s