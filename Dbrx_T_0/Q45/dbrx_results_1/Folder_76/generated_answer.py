def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, min(5, len(s))):
        for j in range(i, min(5, len(s))):
            substring = s[i - 1:j].lower()
            if set(substring).issubset(english_letters):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes