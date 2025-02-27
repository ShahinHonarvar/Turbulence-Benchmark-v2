def remove_repeat_chars(s):
    char_indices = {}
    for i in range(32, 99):
        if s[i] in char_indices:
            char_indices[s[i]].append(i)
        else:
            char_indices[s[i]] = [i]
    for char, indices in char_indices.items():
        if len(indices) > 1:
            s = ''.join([c for c in s if c != char])
    return s