def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:301].lower()
    for i in range(len(s)):
        for j in range(i + 50, min(i + 61, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result