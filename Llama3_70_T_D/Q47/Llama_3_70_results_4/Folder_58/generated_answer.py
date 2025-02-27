def palindromes_of_specific_lengths(s):
    substring = s[125:284].lower()
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes