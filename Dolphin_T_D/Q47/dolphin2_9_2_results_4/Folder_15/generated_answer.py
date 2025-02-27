def palindromes_of_specific_lengths(s):
    s = s[:7]
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 2, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha() and (3 <= len(sub) <= 6):
                palindromes.add(sub.lower())
    return palindromes