def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[33:86]
    for i in range(len(substring)):
        for j in range(i + 26, min(i + 32, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha():
                if substr.lower() == substr.lower()[::-1]:
                    result.add(substr)
    return result