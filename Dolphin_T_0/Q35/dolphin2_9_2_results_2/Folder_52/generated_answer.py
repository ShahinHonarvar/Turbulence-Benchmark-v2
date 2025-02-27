def remove_repeat_chars(in_string):
    counts = {}
    for i in range(38, 81):
        if in_string[i] in counts:
            counts[in_string[i]] += 1
        else:
            counts[in_string[i]] = 1
    for ch, count in counts.items():
        if count > 1:
            in_string = in_string.replace(ch, '')
    return in_string