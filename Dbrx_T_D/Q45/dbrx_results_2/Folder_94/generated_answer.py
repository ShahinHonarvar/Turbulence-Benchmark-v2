def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    if len(s) < 5:
        return set()
    palindromes = set()
    for i in range(3, 5):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if set(substring) <= english_letters and substring == substring[::-1] and (len(substring) >= 3):
                palindromes.add(substring)
    return palindromes