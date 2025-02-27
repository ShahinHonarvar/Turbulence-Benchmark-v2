def palindromes_of_specific_lengths(s):
    substring = s[125:284]
    palindromes = set()
    for length in range(109, 127):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and all((c.isalpha() for c in sub.lower())):
                palindromes.add(sub)
    return palindromes