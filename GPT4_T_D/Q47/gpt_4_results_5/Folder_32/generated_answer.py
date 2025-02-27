import re
    from collections import deque

def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    s = re.sub('[^a-z]', '', s)
    results = set()
    for i in range(len(s)):
        for j in range(43, min(len(s) - i + 1, 48)):
            sub = s[i:i + j]
            if sub == ''.join(deque(sub)):
                results.add(sub)
    return results