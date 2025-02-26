def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:7].lower()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 7, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result