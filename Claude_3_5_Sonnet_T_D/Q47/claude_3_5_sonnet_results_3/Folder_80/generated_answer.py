def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[35:89]
    for i in range(len(substring)):
        for j in range(i + 24, min(i + 34, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha():
                if substr.lower() == substr.lower()[::-1]:
                    result.add(substr)
    return result