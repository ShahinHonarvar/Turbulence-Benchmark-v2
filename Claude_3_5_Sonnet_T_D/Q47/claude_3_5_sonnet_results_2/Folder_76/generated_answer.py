def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[101:293]
    for i in range(len(substring)):
        for j in range(i + 154, min(i + 183, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                result.add(substr)
    return result