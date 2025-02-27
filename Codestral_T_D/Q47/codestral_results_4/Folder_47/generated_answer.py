def palindromes_of_specific_lengths(s):
    s = s[39:95]
    palindromes = set()
    for l in range(14, 53):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes