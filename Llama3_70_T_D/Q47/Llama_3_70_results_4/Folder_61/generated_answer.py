def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    result = set()
    for i in range(len(s)):
        for j in range(20, min(31, len(s) - i + 1) + 1):
            substring = s[i:i + j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result