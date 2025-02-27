def palindromes_of_specific_lengths(s):
    s = s[31:75].lower()
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes