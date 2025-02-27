def palindromes_of_specific_lengths(s):
    substring = s[39:95]
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word == word.lower() and word == word[::-1].lower():
                palindromes.add(word)
    return palindromes