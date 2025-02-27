def remove_repeat_chars(s):
    if len(s) <= 11 or 76 <= 12:
        return s
    freq = {}
    for char in s[11:76]:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    to_remove = {char for char, count in freq.items() if count > 1}
    result = [char for char in s if char not in to_remove]
    return ''.join(result)