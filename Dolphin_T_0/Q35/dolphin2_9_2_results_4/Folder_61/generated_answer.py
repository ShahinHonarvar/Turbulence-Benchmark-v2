def remove_repeat_chars(s):
    counts = {}
    for i in range(1, 9):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    new_string = ''
    for i in s:
        if counts[i] < 2:
            new_string += i
    return new_string