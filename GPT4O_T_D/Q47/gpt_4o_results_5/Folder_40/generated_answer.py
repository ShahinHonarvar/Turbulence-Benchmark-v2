def palindromes_of_specific_lengths(s):
    s = s[:6].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 6, len(s))):
            substr = s[i:j + 1]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result