from collections import defaultdict

def all_substring_of_size_n(s):
    result = []
    count = defaultdict(int)
    n = len(s)
    for i in range(n):
        for j in range(i + 124, n + 1):
            substring = s[i:j]
            if len(substring) == 124 and len(set(substring)) == 124:
                result.append(substring)
                count[substring] += 1
    return result