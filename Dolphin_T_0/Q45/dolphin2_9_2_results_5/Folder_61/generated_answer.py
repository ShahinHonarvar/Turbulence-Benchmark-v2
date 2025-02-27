import string

def palindromes_between_indices(s):
    letters = set()
    for c in s[:8]:
        if c.isalpha():
            letters.add(c.lower())
    result = set()
    length = 7
    if len(letters) < length // 2:
        return result
    for i in range(length):
        sub = s[i:i + length]
        if sub == sub[::-1]:
            result.add(sub)
    return result