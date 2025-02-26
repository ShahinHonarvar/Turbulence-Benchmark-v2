def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[70:141]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 61, len(substring) + 1)):
            substr = substring[i:j]
            if substr.isalpha():
                if substr.lower() == substr.lower()[::-1]:
                    result.add(substr)
    return result