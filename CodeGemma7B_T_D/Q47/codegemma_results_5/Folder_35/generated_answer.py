from string import ascii_lowercase

def palindromes_of_specific_lengths(s):
    s = s.lower()
    res = set()
    for i in range(34, 91):
        for j in range(i - 13 + 1, i + 1):
            if j - i < 14 or i - j < 14:
                continue
            if ''.join(ascii_lowercase[i - j:j + 1]) in s:
                res.add(''.join(ascii_lowercase[i - j:j + 1]))
    return res