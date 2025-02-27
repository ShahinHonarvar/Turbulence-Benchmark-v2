def palindromes_between_indices(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 5):
        for j in range(i, 5):
            substring = string[i:j + 1].lower()
            if set(substring).issubset(english_letters) and len(substring) >= 5:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes