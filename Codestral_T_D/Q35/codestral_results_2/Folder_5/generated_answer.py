def remove_repeat_chars(s):
    mid_s = s[2:8]
    seen = {}
    for char in mid_s:
        if char in seen:
            seen[char] += 1
        else:
            seen[char] = 1
    repeat_chars = [char for char, count in seen.items() if count > 1]
    return ''.join((char for char in s if char not in repeat_chars))