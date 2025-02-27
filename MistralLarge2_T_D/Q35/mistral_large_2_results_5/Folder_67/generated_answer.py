def remove_repeat_chars(s):
    substring = s[44:67]
    counts = {}
    for char in substring:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    repeats = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in repeats))