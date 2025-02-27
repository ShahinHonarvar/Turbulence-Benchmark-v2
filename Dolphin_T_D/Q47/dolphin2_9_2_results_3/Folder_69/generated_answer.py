def palindromes_of_specific_lengths(s):
    substring = s[11:97]
    palindromes = set()
    for i in range(11, len(substring) - 44):
        for length in range(45, 53):
            sub = substring[i:i + length]
            if sub == sub.lower() and sub == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes