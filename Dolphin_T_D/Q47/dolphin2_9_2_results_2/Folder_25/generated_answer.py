def palindromes_of_specific_lengths(s):
    substring = s[25:85]
    palindromes = set()
    for i in range(30, 47):
        for j in range(0, len(substring) - i + 1):
            sub = substring[j:j + i]
            if all((c.isalpha() for c in sub)) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes