def palindromes_of_specific_lengths(s):
    substring = s[18:66]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 37, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha():
                if substr.lower() == substr.lower()[::-1]:
                    result.add(substr)
    return result