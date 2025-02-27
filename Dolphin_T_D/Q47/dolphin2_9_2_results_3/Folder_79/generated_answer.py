def palindromes_of_specific_lengths(s):
    substring = s[1:9]
    palindromes = set()
    for length in range(3, 5):
        for index in range(len(substring) - length + 1):
            sub = substring[index:index + length]
            if all((c.isalpha() for c in sub)) or all((c.isalpha() and c.islower() for c in sub)):
                if sub == sub[::-1]:
                    palindromes.add(sub.lower())
    return palindromes