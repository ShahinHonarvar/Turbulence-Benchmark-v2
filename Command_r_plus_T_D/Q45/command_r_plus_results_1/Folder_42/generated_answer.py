def palindromes_between_indices(s):
    s = s[6:10].lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_letters = set(s)
    if not s_letters.issubset(english_letters):
        return set()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes