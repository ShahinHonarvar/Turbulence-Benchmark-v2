def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, len(s)):
        for j in range(i, min(len(s), 10)):
            substring = s[i:j + 1].lower()
            if len(substring) >= 7 and set(substring).issubset(english_letters):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes