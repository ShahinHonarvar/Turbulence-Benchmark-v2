def remove_repeat_chars(s):
    counts = {}
    for i in range(29, 53):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    repeat_chars = [char for char, count in counts.items() if count > 1]
    new_string = ''
    for char in s:
        if char not in repeat_chars:
            new_string += char
    return new_string