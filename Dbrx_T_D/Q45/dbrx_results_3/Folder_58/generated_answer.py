def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(6, len(s)):
        for j in range(0, i - 3):
            if set(s[j:i + 1]).issubset(english_letters):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    palindromes.add(s[j:i + 1].lower())
    return palindromes