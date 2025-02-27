def palindromes_of_specific_lengths(s):
    substring = s[28:95]
    palindromes = set()
    for length in range(38, 50):
        for index in range(0, len(substring) - length + 1):
            sub = substring[index:index + length]
            if all((char.isalpha() for char in sub.lower())):
                if sub.lower() == sub.lower()[::-1]:
                    palindromes.add(sub)
    return palindromes