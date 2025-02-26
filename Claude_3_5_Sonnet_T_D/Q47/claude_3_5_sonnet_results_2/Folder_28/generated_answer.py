def palindromes_of_specific_lengths(s):
    substring = s[32:72]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 33, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha():
                if substr.lower() == substr.lower()[::-1]:
                    result.add(substr)
    return result