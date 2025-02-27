def palindromes_of_specific_lengths(s):
    s = s[2:9]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha() and (3 <= len(sub) <= 4):
                palindromes.add(sub.lower())
    return palindromes