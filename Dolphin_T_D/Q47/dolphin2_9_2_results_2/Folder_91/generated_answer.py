def palindromes_of_specific_lengths(s):
    s = s[:11]
    palindromes = set()
    for i in range(len(s) - 2):
        for j in range(i + 3, min(i + 6, len(s) + 1)):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes