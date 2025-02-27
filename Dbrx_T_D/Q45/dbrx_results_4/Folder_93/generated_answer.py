from collections import defaultdict

def palindromes_between_indices(s):
    sub_s = s[2:8].lower()
    freq = defaultdict(int)
    for c in sub_s:
        freq[c] += 1
    result = set()
    for i in range(len(sub_s)):
        for j in range(i, len(sub_s)):
            if sub_s[i:j + 1] in result:
                continue
            if all((freq[c] >= sub_s[i:j + 1].count(c) for c in sub_s[i:j + 1])) and len(sub_s[i:j + 1]) >= 6:
                result.add(sub_s[i:j + 1])
    return result