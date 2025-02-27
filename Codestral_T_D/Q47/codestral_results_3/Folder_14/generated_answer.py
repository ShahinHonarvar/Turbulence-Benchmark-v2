def palindromes_of_specific_lengths(s):
    substring = s[10:75]
    palindromes = set()
    for length in range(6, 9):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes