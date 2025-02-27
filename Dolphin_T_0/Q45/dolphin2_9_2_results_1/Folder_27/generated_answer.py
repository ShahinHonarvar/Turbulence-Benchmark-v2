import string

def palindromes_between_indices(s):
    letters = set(s[2:9].lower())
    res = set()
    if letters.issubset(set(string.ascii_lowercase)):
        for length in range(6, len(s[2:9]) + 1):
            for i in range(len(s[2:9]) - length + 1):
                substring = s[2 + i:2 + i + length]
                if all((c in letters for c in substring.lower())):
                    res.add(substring)
    return res