def palindromes_of_specific_lengths(s):
    substr = s[16:61].lower()
    palindromes = set()
    for length in range(16, 40):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes