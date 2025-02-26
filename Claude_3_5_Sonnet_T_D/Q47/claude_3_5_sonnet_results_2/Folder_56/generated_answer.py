def palindromes_of_specific_lengths(s):
    result = set()
    s = s[1:10].upper()
    for i in range(len(s)):
        for j in range(i + 3, min(i + 8, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr.lower())
    return result