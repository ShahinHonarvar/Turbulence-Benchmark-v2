def palindromes_of_specific_lengths(s):
    substring = s[27:78]
    palindromes = set()
    for length in range(18, 20):
        for i in range(len(substring)):
            word = substring[i:i + length]
            if word == word.lower() and word[::-1] == word:
                palindromes.add(word.lower())
    return palindromes