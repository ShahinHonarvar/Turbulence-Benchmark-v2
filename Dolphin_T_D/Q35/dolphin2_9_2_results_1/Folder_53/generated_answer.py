def remove_repeat_chars(s):
    chars = [s[i] for i in range(len(s)) if i not in range(200, 203)]
    freq = {}
    for i in range(203, len(s)):
        freq[s[i]] = freq.get(s[i], 0) + 1
    for char, count in freq.items():
        if count > 1 and char in chars:
            chars = [c for c in chars if c != char]
    return ''.join(chars)