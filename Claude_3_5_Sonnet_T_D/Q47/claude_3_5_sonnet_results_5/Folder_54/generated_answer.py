def palindromes_of_specific_lengths(s):
    substring = s[27:78]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 18, i + 20):
            if j <= len(substring):
                substr = substring[i:j]
                if substr.isalpha():
                    if substr.lower() == substr.lower()[::-1]:
                        palindromes.add(substr)
    return palindromes