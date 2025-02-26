def palindromes_of_specific_lengths(s):
    result = set()
    s = s[17:96].lower()
    for i in range(len(s)):
        for j in range(i + 13, min(i + 50, len(s) + 1)):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result