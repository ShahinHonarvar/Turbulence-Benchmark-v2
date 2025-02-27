def palindromes_of_specific_lengths(s):
    substring = s[125:284]
    lengths = range(109, 127)
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes