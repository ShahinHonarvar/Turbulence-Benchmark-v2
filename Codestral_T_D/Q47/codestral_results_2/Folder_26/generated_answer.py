def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[24:85].lower()
    for length in range(21, 32):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes