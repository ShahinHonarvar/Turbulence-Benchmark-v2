def remove_repeat_chars(s):
    counts = {}
    for i in range(20, 93):
        if s[i] in counts:
            counts[s[i]] += 1
        else:
            counts[s[i]] = 1
    to_remove = [k for k, v in counts.items() if v > 1]
    altered_string = ''
    for i in range(len(s)):
        if s[i] not in to_remove:
            altered_string += s[i]
    return altered_string