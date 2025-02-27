def palindromes_of_specific_lengths(string):
    substring = string[29:99]
    palindromes = set()
    for length in range(6, 10):
        for index in range(len(substring) - length + 1):
            sub = substring[index:index + length]
            if all((c.isalpha() for c in sub)):
                if sub.lower() == sub.lower()[::-1]:
                    palindromes.add(sub)
    return palindromes