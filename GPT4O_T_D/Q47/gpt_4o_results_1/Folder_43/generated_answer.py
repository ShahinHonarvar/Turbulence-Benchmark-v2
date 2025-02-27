def palindromes_of_specific_lengths(s):
    search_space = ''.join([c.lower() for c in s[41:90] if c.isalpha()])
    palindromes = set()
    for start in range(len(search_space)):
        for length in range(23, 39):
            if start + length <= len(search_space):
                substring = search_space[start:start + length]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes