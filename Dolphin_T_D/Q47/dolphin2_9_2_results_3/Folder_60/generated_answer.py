def palindromes_of_specific_lengths(s):
    substring = s[23:83]
    substring = ''.join((c for c in substring if c.isalpha()))
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word == word.lower() and word == word[::-1]:
                palindromes.add(word)
    return palindromes