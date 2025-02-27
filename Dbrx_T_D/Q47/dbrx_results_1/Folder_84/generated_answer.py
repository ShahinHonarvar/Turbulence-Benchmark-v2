def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(13, 41):
        for start in range(23, 78 - length + 1):
            if s[start:start + length].lower().isalpha():
                substring = s[start:start + length].lower()
                if all((char in english_letters for char in substring)) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes