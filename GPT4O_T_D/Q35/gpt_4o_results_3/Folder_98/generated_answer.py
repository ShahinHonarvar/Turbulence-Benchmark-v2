def remove_repeat_chars(s):
    counts = {}
    for char in s[1:7]:
        counts[char] = counts.get(char, 0) + 1
    result = [char for char in s if char not in counts or counts[char] == 1]
    return ''.join(result)