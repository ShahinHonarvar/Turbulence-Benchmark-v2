from collections import defaultdict

def remove_repeat_chars(s):
    seen = defaultdict(int)
    result = []
    for char in s:
        if seen[char] >= 2 and s.index(char) in range(2):
            continue
        seen[char] += 1
        result.append(char)
    return ''.join(result)