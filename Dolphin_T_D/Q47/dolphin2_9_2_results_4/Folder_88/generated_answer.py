def palindromes_of_specific_lengths(s):
    substring = s[11:88]
    palindromes = set()
    for i in range(len(substring) - 4):
        sub = substring[i:i + 5]
        if all((c.isalpha() for c in sub)) and sub.lower() == sub[::-1].lower():
            palindromes.add(sub.lower())
    if len(palindromes) > 0:
        return palindromes
    else:
        return set()