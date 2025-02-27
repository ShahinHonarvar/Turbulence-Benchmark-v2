def palindromes_of_specific_lengths(text):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(40, 95):
        for length in range(45, 52):
            if i + length <= 94:
                substring = text[i:i + length]
                substring_set = set(substring)
                if substring_set.issubset(english_letters) and substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes