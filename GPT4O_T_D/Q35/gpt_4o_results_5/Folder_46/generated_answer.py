def remove_repeat_chars(s):
    if len(s) <= 11:
        return s
    sub_string = s[11:79]
    freq = {}
    for char in sub_string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    repeated_chars = {char for char in freq if freq[char] > 1}
    return ''.join((char for char in s if char not in repeated_chars or s.index(char) <= 10 or s.index(char) >= 79))