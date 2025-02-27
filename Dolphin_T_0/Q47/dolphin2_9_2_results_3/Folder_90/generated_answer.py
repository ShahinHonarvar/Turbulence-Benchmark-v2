def palindromes_of_specific_lengths(string):
    substring = string[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(substring)):
            word = substring[i:i + length]
            if word == word[::-1] and word.isalpha():
                palindromes.add(word)
    return palindromes