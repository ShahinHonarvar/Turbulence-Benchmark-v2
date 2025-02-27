def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(10, 56):
        for j in range(i + 3, min(i + 8, 56)):
            substring = s[i:j]
            if all((c.isalpha() for c in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes