def remove_repeat_chars(s):
    counts = {}
    for char in s[1:3]:
        counts[char] = counts.get(char, 0) + 1
    return ''.join((char for char in s if counts.get(char, 0) <= 1))