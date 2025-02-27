def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 2):
        for j in range(i + 2, len(s)):
            substring = s[i:j + 1].lower()
            if set(substring).issubset(english_letters):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes