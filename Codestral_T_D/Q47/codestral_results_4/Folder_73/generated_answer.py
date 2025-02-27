def palindromes_of_specific_lengths(s):
    s = s[21:63].lower()
    palindromes = set()
    for l in range(22, 34):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes