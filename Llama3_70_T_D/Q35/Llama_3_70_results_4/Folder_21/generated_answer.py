def remove_repeat_chars(s):
    chars = list(s)
    counts = {}
    for i in range(462, 995):
        if chars[i] in counts:
            counts[chars[i]] += 1
        else:
            counts[chars[i]] = 1
    to_remove = [char for char, count in counts.items() if count > 1]
    for char in to_remove:
        chars = [c for c in chars if c != char]
    return ''.join(chars)