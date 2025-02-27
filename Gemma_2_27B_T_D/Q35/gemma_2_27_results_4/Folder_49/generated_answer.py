def remove_repeat_chars(s):
    seen = set()
    counts = {}
    for i in range(end):
        if 90 <= i < 200:
            if s[i] in counts:
                counts[s[i]] += 1
            else:
                counts[s[i]] = 1
    for char in counts:
        if counts[char] > 1:
            seen.add(char)
    result = []
    for char in s:
        if char not in seen:
            result.append(char)
    return ''.join(result)