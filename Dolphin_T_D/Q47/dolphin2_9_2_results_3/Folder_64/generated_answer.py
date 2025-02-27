def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[0:8]
    for length in range(4, 6):
        for i in range(len(substring)):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes