def palindromes_of_specific_lengths(s):
    substring = s[41:90]
    palindromes = set()
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word == word.lower() and word == word.upper():
                palindromes.add(word)
    return palindromes