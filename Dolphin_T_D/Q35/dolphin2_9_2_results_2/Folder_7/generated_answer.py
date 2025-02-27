def remove_repeat_chars(s):
    counts = {}
    for i in range(375, 926):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    chars_to_remove = []
    for char, count in counts.items():
        if count > 1:
            chars_to_remove.append(char)
    new_string = ''
    for char in s:
        if char not in chars_to_remove:
            new_string += char
    return new_string