def remove_repeat_chars(s):
    counts = {}
    for i in range(10, 76):
        if i < len(s):
            char = s[i]
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    result = [char for char in s if counts.get(char, 0) <= 1]
    return ''.join(result)