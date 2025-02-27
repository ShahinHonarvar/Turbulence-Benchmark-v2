def palindromes_of_specific_lengths(text):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(106, 281):
        for j in range(i + 136, i + 152):
            if i + j >= len(text):
                continue
            substring = text[i:j].lower()
            if substring == substring[::-1] and all((char in letters for char in substring)):
                palindromes.add(substring)
    return palindromes