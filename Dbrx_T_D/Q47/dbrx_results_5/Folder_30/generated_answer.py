def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(14, 91):
        for j in range(55, 72):
            if i + j - 1 <= 90:
                substring = s[i:i + j]
                if substring.lower() == substring.lower()[::-1] and set(substring).issubset(english_letters):
                    palindromes.add(substring)
    return palindromes