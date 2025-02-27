def palindromes_of_specific_lengths(s):
    substring = s[23:83]
    palindromes = set()
    for length in range(32, 35):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes