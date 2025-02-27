def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[27:78]
    for length in range(18, 20):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes