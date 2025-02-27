def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(32, 80):
        for j in range(i + 34, min(i + 42, 80)):
            substr = s[i:j + 1]
            if all((c.isalpha() for c in substr.lower())):
                if substr.lower() == substr.lower()[::-1]:
                    palindromes.add(substr)
    return palindromes