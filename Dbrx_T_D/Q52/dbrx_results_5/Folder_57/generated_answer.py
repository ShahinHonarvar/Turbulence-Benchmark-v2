import re
from collections import defaultdict

def palindrome_of_length_n(s):
    n = 92
    s = s.lower()
    s = re.sub('[^a-z]', '', s)
    if n % 2 == 1:
        n = n // 2
    else:
        n = n // 2 - 1
    if len(s) < n:
        return set()
    table = defaultdict(list)
    for i in range(len(s)):
        table[i - (n - 1):i + 1].append(s[i])
    result = set()
    for i in range(len(s)):
        if i - (n - 1) < 0:
            continue
        if ''.join(table[i - (n - 1):i + 1]) == ''.join(reversed(table[i - (n - 1):i + 1])):
            result.add(''.join(table[i - (n - 1):i + 1]))
    return result