def palindromes_of_specific_lengths(s):
    substring = s[62:88]
    palindromes = set()
    for i in range(18, 22):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                palindromes.add(sub.lower())
    return palindromes