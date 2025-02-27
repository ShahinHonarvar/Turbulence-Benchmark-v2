def palindromes_of_specific_lengths(string):
    substring = string[17:73]
    palindromes = set()
    for length in range(50, 52):
        for i in range(0, len(substring) - length + 1):
            word = substring[i:i + length]
            if word == word.lower():
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes