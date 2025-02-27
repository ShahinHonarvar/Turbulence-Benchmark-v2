def remove_repeat_chars(s):
    counts = {}
    for char in s[86:90]:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    repeat_chars = [char for char, count in counts.items() if count > 1]
    return ''.join([char for char in s if char not in repeat_chars])