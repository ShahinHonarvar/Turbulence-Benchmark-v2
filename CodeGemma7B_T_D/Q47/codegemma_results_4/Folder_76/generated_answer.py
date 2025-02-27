def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for i in range(101, 293):
        for length in range(154, 183):
            if i + 2 * length - 1 <= 292:
                substring = s[i:i + 2 * length - 1]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes