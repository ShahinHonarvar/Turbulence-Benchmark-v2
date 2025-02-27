def palindromes_of_specific_lengths(s):
    s = s[28:95]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 38, i + 50):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes