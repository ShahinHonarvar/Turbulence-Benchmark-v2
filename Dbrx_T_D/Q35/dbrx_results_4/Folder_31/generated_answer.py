def remove_repeat_chars(s: str) -> str:
    char_freq = {}
    result = s[:33] + s[78:]
    for i in range(33, 78):
        if s[i] in char_freq:
            char_freq[s[i]] += 1
        else:
            char_freq[s[i]] = 1
    for char, freq in char_freq.items():
        if freq > 1:
            result = result.replace(char, '', freq - 1)
    return result