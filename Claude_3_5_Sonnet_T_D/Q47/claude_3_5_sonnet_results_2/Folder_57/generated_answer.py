def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:95]
    for i in range(len(substring)):
        for j in range(i + 39, min(i + 53, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha() and substr.lower() == substr.lower()[::-1]:
                result.add(substr)
    return result