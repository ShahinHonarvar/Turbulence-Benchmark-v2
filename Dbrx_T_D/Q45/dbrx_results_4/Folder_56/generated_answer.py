from collections import defaultdict

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    chars = defaultdict(int)
    for i in range(5, 10):
        chars[s[i].lower()] += 1
    result = set()
    for char in chars:
        if chars[char] >= 5:
            result.add(char * 5)
        elif chars[char] >= 2:
            for other in chars:
                if other != char and chars[other] > 0:
                    result.add(char * 2 + other + char * 2)
                    break
    return result