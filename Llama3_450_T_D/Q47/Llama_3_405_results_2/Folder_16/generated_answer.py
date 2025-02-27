def palindromes_of_specific_lengths(s):
    s = s[15:87]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 51, min(i + 61, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr.casefold() == substr.casefold()[::-1]:
                palindromes.add(substr)
    return palindromes