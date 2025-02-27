def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[23:78]
    palindromes = set()
    for length in range(13, 41):
        for i in range(len(substr) - length + 1):
            sub = substr[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes