def palindromes_of_specific_lengths(s):
    substring = s[17:73]
    palindromes = set()
    for length in range(50, 52):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if all((c.isalpha() for c in sub)) and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes