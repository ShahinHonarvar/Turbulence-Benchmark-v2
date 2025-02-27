def palindromes_of_specific_lengths(s):
    s = s[23:83].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 32, min(i + 35, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result