def palindromes_of_specific_lengths(s):
    palindromes = set()
    substr = s[16:61]
    for length in range(16, 40):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.lower() == sub[::-1].lower() and sub.isalpha():
                palindromes.add(sub)
    return palindromes