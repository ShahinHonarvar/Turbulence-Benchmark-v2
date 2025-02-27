def palindromes_between_indices(s):
    english_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(4, 6):
        for j in range(i, 7):
            substring = s[i:j + 1].lower()
            if all((char in english_lowercase_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes