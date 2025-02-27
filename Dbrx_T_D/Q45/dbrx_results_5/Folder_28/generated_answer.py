from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    chars = defaultdict(int)
    for i in range(1, 6):
        chars[s[i]] += 1
    palindromes = set()
    for i in range(4, len(s) - 1):
        candidates = [char * i for char in chars.keys() if chars[char] >= i]
        for candidate in candidates:
            if candidate[::-1] == candidate:
                palindromes.add(candidate)
    return palindromes