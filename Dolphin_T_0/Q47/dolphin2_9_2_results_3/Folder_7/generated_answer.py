def palindromes_of_specific_lengths(string):
    substring = string[119:257]
    lengths = range(104, 124)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            sub = sub.lower()
            if all((c.isalpha() for c in sub)) and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes