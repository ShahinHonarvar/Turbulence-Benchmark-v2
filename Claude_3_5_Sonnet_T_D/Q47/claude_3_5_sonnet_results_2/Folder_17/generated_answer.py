def palindromes_of_specific_lengths(s):
    subset = s[22:96]
    palindromes = set()
    for i in range(len(subset)):
        for j in range(i + 52, min(i + 56, len(subset) + 1)):
            substring = subset[i:j]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes