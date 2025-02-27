def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(21):
        for j in range(i + 5, min(i + 81, len(string) + 1)):
            substring = string[i:j]
            if len(substring) >= 5 and substring.lower() == substring.lower()[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring)
    return palindromes