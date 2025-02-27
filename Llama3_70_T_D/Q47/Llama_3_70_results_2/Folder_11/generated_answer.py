def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes