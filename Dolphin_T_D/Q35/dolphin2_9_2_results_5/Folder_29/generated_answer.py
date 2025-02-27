def remove_repeat_chars(s):
    counts = {}
    for char in s[70:98]:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    repeat_chars = [char for char, count in counts.items() if count > 1]
    s = ''.join([char for char in s if char not in repeat_chars])
    return s