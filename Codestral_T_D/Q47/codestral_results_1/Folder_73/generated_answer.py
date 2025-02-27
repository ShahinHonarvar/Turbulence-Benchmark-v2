def palindromes_of_specific_lengths(s):
    s = s[21:63]
    palindromes = set()
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes