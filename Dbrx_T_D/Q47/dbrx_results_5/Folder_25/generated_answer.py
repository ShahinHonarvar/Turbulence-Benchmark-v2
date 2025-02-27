def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(26, 85):
        for length in range(30, 47):
            if i + length - 1 <= 84:
                substring = s[i:i + length]
                if all((char in english_letters for char in substring)):
                    if substring.lower() == substring.lower()[::-1]:
                        palindromes.add(substring)
    return palindromes