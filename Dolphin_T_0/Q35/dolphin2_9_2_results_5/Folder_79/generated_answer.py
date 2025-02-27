def remove_repeat_chars(s):
    occurrences = {}
    for i in range(1, 7):
        if s[i] in occurrences:
            occurrences[s[i]] += 1
        else:
            occurrences[s[i]] = 1
    for char in occurrences:
        if occurrences[char] > 1:
            s = s.replace(char, '')
    return s