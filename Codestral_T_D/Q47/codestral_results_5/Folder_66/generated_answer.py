def palindromes_of_specific_lengths(s):
    s = s[32:80].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 35, min(i + 42, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)
    return palindromes