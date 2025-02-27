def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes