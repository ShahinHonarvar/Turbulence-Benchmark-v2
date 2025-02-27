def palindromes_of_specific_lengths(s):
    substring = s[11:94]
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if all((x.isalpha() and x.lower() == x for x in word)) and word == word[::-1]:
                palindromes.add(word)
    return palindromes