def remove_repeat_chars(s):
    substring = s[28:96]
    counts = {}
    for char in substring:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    to_remove = {char for char, count in counts.items() if count > 1}
    result = ''.join((char for char in s if char not in to_remove or s.index(char) <= 27 or s.index(char) >= 96))
    return result