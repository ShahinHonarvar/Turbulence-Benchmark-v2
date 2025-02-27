def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[32:80].lower()
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes