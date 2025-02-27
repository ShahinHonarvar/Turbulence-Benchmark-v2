def remove_repeat_chars(s):
    char_index = {}
    for i in range(16, 87):
        if s[i] not in char_index:
            char_index[s[i]] = [i]
        else:
            char_index[s[i]].append(i)
    to_remove = []
    for char, indices in char_index.items():
        if len(indices) > 1:
            to_remove.extend(indices)
    to_remove = sorted(list(set(to_remove)), reverse=True)
    new_s = ''
    for i, char in enumerate(s):
        if i not in to_remove:
            new_s += char
    return new_s