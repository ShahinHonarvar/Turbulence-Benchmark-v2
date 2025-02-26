def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 14, min(i + 40, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha():
                if substr.lower() == substr.lower()[::-1]:
                    palindromes.add(substr)
    return palindromes