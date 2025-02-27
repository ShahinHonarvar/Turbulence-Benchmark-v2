def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(31, 75):
        for j in range(i, min(len(s), i + 39)):
            substring = s[i:j + 1]
            if all((c.isalpha() for c in substring)):
                lowercase = substring.lower()
                if lowercase == lowercase[::-1]:
                    palindromes.add(substring)
    return palindromes