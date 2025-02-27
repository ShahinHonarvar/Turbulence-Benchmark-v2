def palindromes_of_specific_lengths(s):
    substring = s[74:96]
    palindromes = set()
    for length in range(7, 10):
        for start in range(len(substring) - length + 1):
            sub = substring[start:start + length]
            if sub.lower() == sub[::-1].lower():
                if sub.isalpha():
                    palindromes.add(sub)
    return palindromes