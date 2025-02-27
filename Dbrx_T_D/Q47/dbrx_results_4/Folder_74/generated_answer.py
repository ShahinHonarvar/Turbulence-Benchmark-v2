def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(30, 85):
        for j in range(12, 21):
            if i + j - 1 <= 84:
                substring = string[i:i + j].lower()
                if substring and english_letters.issuperset(substring) and (substring == substring[::-1]):
                    palindromes.add(substring)
    return palindromes