def palindromes_of_specific_lengths(s):
    substring = s[45:99]
    lengths = range(40, 48)
    palindromes = set()
    for length in lengths:
        for i in range(0, len(substring) - length + 1):
            word = substring[i:i + length]
            if all((char.isalpha() and word.lower() == word[::-1].lower() for char in word)):
                palindromes.add(word)
    return palindromes