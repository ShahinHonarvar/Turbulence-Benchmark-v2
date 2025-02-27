from collections import defaultdict

def is_english_letter(c):
    return c.lower() >= 'a' and c.lower() <= 'z'

def palindrome_of_length_n(s, n):
    if n % 2 == 1:
        return set()
    s = s.lower()
    palindromes = set()
    letters = defaultdict(list)
    for i, c in enumerate(s):
        if is_english_letter(c):
            letters[c].append(i)
    for pair in letters.values():
        for i in range(len(pair) - n + 2):
            start, end = (pair[i], pair[i + n - 1])
            if end - start + 1 == n and s[start:end + 1] == s[start:end + 1][::-1]:
                palindromes.add(s[start:end + 1])
    return palindromes