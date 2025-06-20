def palindromes_of_specific_lengths(s):
    substring = s[40:90]
    palindromes = set()
    for length in range(23, 39):
        for i in range(0, len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes