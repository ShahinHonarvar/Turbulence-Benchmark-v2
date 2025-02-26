def palindromes_of_specific_lengths(s):
    substring = s[10:71]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 24, min(i + 53, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                palindromes.add(substr)
    return palindromes