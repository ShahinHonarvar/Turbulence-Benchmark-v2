def palindromes_of_specific_lengths(s):
    substring = s[30:85]
    palindromes = set()
    for i in range(len(substring) - 20 + 1):
        for length in range(12, 21):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes