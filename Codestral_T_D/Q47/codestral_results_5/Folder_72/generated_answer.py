def palindromes_of_specific_lengths(string):
    substring = string[26:91]
    palindromes = set()
    for length in range(27, 59):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes