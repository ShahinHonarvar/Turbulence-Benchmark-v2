import string

def palindromes_between_indices(s):
    letters = [ch for ch in s[1:6] if ch.isalpha()]
    palindromes = set()
    n = len(letters)
    for i in range(n):
        for j in range(i, n + 1):
            sub = ''.join(letters[i:j])
            if len(sub) >= 4 and sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes