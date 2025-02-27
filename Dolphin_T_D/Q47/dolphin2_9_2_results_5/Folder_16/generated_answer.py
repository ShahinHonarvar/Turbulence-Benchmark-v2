def palindromes_of_specific_lengths(s):
    substring = s[15:87]
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((c.isalpha() for c in sub)) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes