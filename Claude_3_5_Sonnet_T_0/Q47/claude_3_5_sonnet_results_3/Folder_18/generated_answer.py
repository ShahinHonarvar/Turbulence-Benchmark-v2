def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:84]
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 67, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                result.add(substr)
    return result