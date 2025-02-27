def palindromes_of_specific_lengths(string):
    substring = string[62:89]
    palindromes = set()
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            sub = ''.join(filter(str.isalpha, sub))
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes