def remove_repeat_chars(s):
    counts = {}
    for c in s[:125] + s[825:]:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    altered_string = ''
    for c in s[:125] + s[825:]:
        if counts[c] == 1:
            altered_string += c
    return altered_string