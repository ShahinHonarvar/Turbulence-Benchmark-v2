def palindromes_of_specific_lengths(s):
    s = s[44:100]
    palindromes = set()
    for l in range(13, 43):
        for i in range(len(s) - l + 1):
            substring = s[i:i + l]
            if all((x.isalpha() for x in substring)):
                substring = substring.lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes