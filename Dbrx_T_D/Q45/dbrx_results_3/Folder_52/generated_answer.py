from collections import defaultdict

def palindromes_between_indices(s):
    s = s.lower()
    eng_letters = {c for c in s if c.isalpha()}
    if len(eng_letters) < 6:
        return set()
    result = set()
    for i in range(8):
        for j in range(i, 8):
            letters = eng_letters & set(s[i:j + 1])
            if len(letters) >= 6:
                palindrome = ''.join(sorted(letters))
                result.add(palindrome[::-1] + palindrome)
    return result