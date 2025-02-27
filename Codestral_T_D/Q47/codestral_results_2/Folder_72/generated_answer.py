def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[26:91].lower()
    for length in range(27, 59):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes