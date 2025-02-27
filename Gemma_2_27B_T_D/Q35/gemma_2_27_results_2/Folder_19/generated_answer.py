def remove_repeat_chars(s):
    char_counts = {}
    for i in range(1, len(s) - 1):
        if s[i] in char_counts:
            char_counts[s[i]] += 1
        else:
            char_counts[s[i]] = 1
    result = []
    for char in s:
        if char in char_counts and char_counts[char] > 1:
            pass
        else:
            result.append(char)
    return ''.join(result)