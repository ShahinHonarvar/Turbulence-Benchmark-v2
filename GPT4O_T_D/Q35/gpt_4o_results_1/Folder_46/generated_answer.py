def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    freq = {}
    for i in range(11, min(79, len(s) - 1)):
        if s[i] in freq:
            freq[s[i]] += 1
        else:
            freq[s[i]] = 1
    chars_to_remove = {char for char, count in freq.items() if count > 1}
    return ''.join((char for char in s if char not in chars_to_remove or not 10 < s.index(char) < 79))