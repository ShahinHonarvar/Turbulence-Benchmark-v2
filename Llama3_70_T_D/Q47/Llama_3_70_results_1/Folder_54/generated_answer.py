def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    palindromes = set()
    for i in range(len(s) - 18 + 1):
        substr = s[i:i + 18]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    for i in range(len(s) - 19 + 1):
        substr = s[i:i + 19]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes