def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[26:85]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i + 30, min(i + 47, len(substr) + 1)):
            sub = substr[i:j]
            if sub.isalpha() and sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes