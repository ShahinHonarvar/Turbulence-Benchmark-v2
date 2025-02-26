def remove_repeat_chars(s):
    freq = {}
    for i in range(28, 96):
        if i < len(s):
            char = s[i]
            freq[char] = freq.get(char, 0) + 1
    repeated_chars = {char for char, count in freq.items() if count > 1}
    result = ''.join((char for char in s if char not in repeated_chars))
    return result